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
- `-y, --yes`: run non-interactively with defaults
- `--overwrite`: overwrite existing PNG files
- `--dry-run`: print output file paths without writing files
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

## Output Naming

- 3D NIfTI: `<basename>_z001.png`, `<basename>_z002.png`, ...
- 4D NIfTI: `<basename>_t001_z001.png`, `<basename>_t001_z002.png`, ...

`<basename>` is derived from input filename without `.nii` / `.nii.gz`.

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
