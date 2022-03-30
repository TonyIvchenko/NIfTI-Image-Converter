# Converter Recipe case020

## Goal
Prepare PNG image slices for case020 using repeatable settings.

## Commands
```bash
cd ~/git/nifti-image-converter
python3 python/nii2png.py \
  -i data/case020.nii.gz \
  -o workspace/images/case020 \
  --axis y \
  --rotate 270 \
  --normalize global \
  --prefix case020 \
  --index-width 3 \
  --manifest-json workspace/images/case020-manifest.json \
  --yes
```

## Integration Notes
- Keep `--prefix`, `--axis`, and `--index-width` aligned with `lungmask` export settings.
- Keep images under `workspace/images/case020` and masks under `workspace/masks/case020`.
