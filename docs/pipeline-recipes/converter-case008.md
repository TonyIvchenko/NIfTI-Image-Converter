# Converter Recipe case008

## Goal
Prepare PNG image slices for case008 using repeatable settings.

## Commands
```bash
cd ~/git/nifti-image-converter
python3 python/nii2png.py \
  -i data/case008.nii.gz \
  -o workspace/images/case008 \
  --axis y \
  --rotate 270 \
  --normalize global \
  --prefix case008 \
  --index-width 3 \
  --manifest-json workspace/images/case008-manifest.json \
  --yes
```

## Integration Notes
- Keep `--prefix`, `--axis`, and `--index-width` aligned with `lungmask` export settings.
- Keep images under `workspace/images/case008` and masks under `workspace/masks/case008`.
