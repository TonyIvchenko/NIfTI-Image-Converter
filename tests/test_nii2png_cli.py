import json
import sys
import types
from pathlib import Path

import numpy as np
import pytest

from importlib.util import module_from_spec, spec_from_file_location


MODULE_PATH = Path(__file__).resolve().parents[1] / "python" / "nii2png.py"
SPEC = spec_from_file_location("nii2png", MODULE_PATH)
nii2png = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(nii2png)


def test_main_dry_run_creates_manifest_without_writing_png(tmp_path, monkeypatch):
    input_path = tmp_path / "scan.nii.gz"
    input_path.write_text("stub", encoding="utf-8")
    output_dir = tmp_path / "png"
    manifest_path = tmp_path / "manifest.json"

    volume = np.arange(3 * 4 * 2).reshape((3, 4, 2)).astype(float)

    class FakeNiftiImage:
        def get_fdata(self):
            return volume

    monkeypatch.setitem(
        sys.modules,
        "nibabel",
        types.SimpleNamespace(load=lambda _: FakeNiftiImage()),
    )

    writes = []
    monkeypatch.setattr(nii2png.imageio, "imwrite", lambda *args, **kwargs: writes.append((args, kwargs)))

    nii2png.main(
        [
            "-i",
            str(input_path),
            "-o",
            str(output_dir),
            "--yes",
            "--dry-run",
            "--axis",
            "y",
            "--manifest-json",
            str(manifest_path),
        ]
    )

    assert writes == []
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["axis"] == "y"
    assert manifest["dry_run"] is True
    assert len(manifest["records"]) == 4
    assert all(record["status"] == "dry_run" for record in manifest["records"])


def test_main_rejects_non_positive_index_width(tmp_path):
    input_path = tmp_path / "scan.nii.gz"
    input_path.write_text("stub", encoding="utf-8")

    with pytest.raises(SystemExit) as exc:
        nii2png.main(["-i", str(input_path), "-o", str(tmp_path / "png"), "--index-width", "0", "--yes"])

    assert exc.value.code == 2
