# NIfTI Image Converter (`nii2png`)

Lightweight tools for converting 3D/4D NIfTI files (`.nii`, `.nii.gz`) into PNG slice stacks.

The repository includes:
- `python/nii2png.py`: command-line converter for Python.
- `matlab/nii2png.m`: interactive converter for Matlab.

## Python Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For development (tests + lint):

```bash
pip install -r requirements-dev.txt
```

## Python Usage

```bash
python3 python/nii2png.py -i <input.nii.gz> -o <output_dir>
```

### CLI options

- `-i, --input`: input NIfTI path (required)
- `-o, --output`: output directory (required)
- `-r, --rotate {0,90,180,270}`: rotate slices by fixed angle
- `--axis {x,y,z}`: slice along selected spatial axis (default: `z`)
- `-y, --yes`: run non-interactively with defaults
- `--overwrite`: overwrite existing PNG files
- `--dry-run`: print output file paths without writing files
- `--normalize {per-slice,global}`: intensity scaling mode (`per-slice` by default)
- `--prefix`: override output basename (default: input filename stem)
- `--index-width`: zero-padding width for slice/volume indices (default: `3`)
- `--manifest-json`: write conversion metadata + slice file records as JSON
- `-q, --quiet`: reduce informational logs

### Examples

Dry run with no prompts:

```bash
python3 python/nii2png.py -i brain.nii.gz -o png --yes --dry-run
```

Rotate and overwrite existing files:

```bash
python3 python/nii2png.py -i fmri.nii -o png --rotate 90 --overwrite
```

Export along the `y` axis with global intensity normalization and a run manifest:

```bash
python3 python/nii2png.py \
  -i ct.nii.gz \
  -o png \
  --axis y \
  --normalize global \
  --manifest-json png/manifest.json \
  --yes
```

## Output Naming

- 3D NIfTI: `<basename>_z001.png`, `<basename>_z002.png`, ...
- 4D NIfTI: `<basename>_t001_z001.png`, `<basename>_t001_z002.png`, ...

`<basename>` is derived from input filename without `.nii` / `.nii.gz`.
`z` changes to `x`/`y` when `--axis x|y` is used.

## Interop Workflow

This repository is intended to pair with:
- `lungmask` for generating mask slices with matching naming/index rules.
- `lung-segmentation` for model training/evaluation on paired `images/` and `masks/` PNG datasets.

Recommended hand-off contract:
1. Convert source volume(s) with fixed `--axis`, `--prefix`, and `--index-width`.
2. Save `--manifest-json` and pass the same naming settings to mask export.
3. Keep converter images and mask images in separate folders while preserving identical filenames.

## Matlab Usage

1. Open Matlab and add `matlab/` to your path.
2. Run:

```matlab
nii2png
```

3. Select working directory and NIfTI file.
4. Choose rotation when prompted.
5. Converted files are saved into `png/` under the selected working directory.

## Development

Run tests:

```bash
pytest -q
```

Run lint:

```bash
ruff check python tests
```

A GitHub Actions workflow (`.github/workflows/python-ci.yml`) runs lint + tests on pushes and pull requests.

## License

MIT, see [LICENSE](LICENSE).
