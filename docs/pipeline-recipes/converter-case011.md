# Converter Recipe case011

## Goal
Prepare PNG image slices for case011 using repeatable settings.

## Commands
```bash
cd ~/git/nifti-image-converter
python3 python/nii2png.py \
  -i data/case011.nii.gz \
  -o workspace/images/case011 \
  --axis y \
  --rotate 180 \
  --normalize per-slice \
  --prefix case011 \
  --index-width 3 \
  --manifest-json workspace/images/case011-manifest.json \
  --yes
```

## Integration Notes
- Keep `--prefix`, `--axis`, and `--index-width` aligned with `lungmask` export settings.
- Keep images under `workspace/images/case011` and masks under `workspace/masks/case011`.
