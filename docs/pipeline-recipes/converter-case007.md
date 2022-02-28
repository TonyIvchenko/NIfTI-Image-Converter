# Converter Recipe case007

## Goal
Prepare PNG image slices for case007 using repeatable settings.

## Commands
```bash
cd ~/git/nifti-image-converter
python3 python/nii2png.py \
  -i data/case007.nii.gz \
  -o workspace/images/case007 \
  --axis x \
  --rotate 180 \
  --normalize per-slice \
  --prefix case007 \
  --index-width 3 \
  --manifest-json workspace/images/case007-manifest.json \
  --yes
```

## Integration Notes
- Keep `--prefix`, `--axis`, and `--index-width` aligned with `lungmask` export settings.
- Keep images under `workspace/images/case007` and masks under `workspace/masks/case007`.
