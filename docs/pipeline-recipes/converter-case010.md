# Converter Recipe case010

## Goal
Prepare PNG image slices for case010 using repeatable settings.

## Commands
```bash
cd ~/git/nifti-image-converter
python3 python/nii2png.py \
  -i data/case010.nii.gz \
  -o workspace/images/case010 \
  --axis x \
  --rotate 90 \
  --normalize global \
  --prefix case010 \
  --index-width 3 \
  --manifest-json workspace/images/case010-manifest.json \
  --yes
```

## Integration Notes
- Keep `--prefix`, `--axis`, and `--index-width` aligned with `lungmask` export settings.
- Keep images under `workspace/images/case010` and masks under `workspace/masks/case010`.
