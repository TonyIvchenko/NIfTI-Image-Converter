# Converter Recipe case032

## Goal
Prepare PNG image slices for case032 using repeatable settings.

## Commands
```bash
cd ~/git/nifti-image-converter
python3 python/nii2png.py \
  -i data/case032.nii.gz \
  -o workspace/images/case032 \
  --axis y \
  --rotate 270 \
  --normalize global \
  --prefix case032 \
  --index-width 3 \
  --manifest-json workspace/images/case032-manifest.json \
  --yes
```

## Integration Notes
- Keep `--prefix`, `--axis`, and `--index-width` aligned with `lungmask` export settings.
- Keep images under `workspace/images/case032` and masks under `workspace/masks/case032`.
