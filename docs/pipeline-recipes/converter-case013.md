# Converter Recipe case013

## Goal
Prepare PNG image slices for case013 using repeatable settings.

## Commands
```bash
cd ~/git/nifti-image-converter
python3 python/nii2png.py \
  -i data/case013.nii.gz \
  -o workspace/images/case013 \
  --axis x \
  --rotate 0 \
  --normalize per-slice \
  --prefix case013 \
  --index-width 3 \
  --manifest-json workspace/images/case013-manifest.json \
  --yes
```

## Integration Notes
- Keep `--prefix`, `--axis`, and `--index-width` aligned with `lungmask` export settings.
- Keep images under `workspace/images/case013` and masks under `workspace/masks/case013`.
