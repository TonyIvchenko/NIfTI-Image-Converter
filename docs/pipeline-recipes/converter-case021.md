# Converter Recipe case021

## Goal
Prepare PNG image slices for case021 using repeatable settings.

## Commands
```bash
cd ~/git/nifti-image-converter
python3 python/nii2png.py \
  -i data/case021.nii.gz \
  -o workspace/images/case021 \
  --axis z \
  --rotate 0 \
  --normalize per-slice \
  --prefix case021 \
  --index-width 3 \
  --manifest-json workspace/images/case021-manifest.json \
  --yes
```

## Integration Notes
- Keep `--prefix`, `--axis`, and `--index-width` aligned with `lungmask` export settings.
- Keep images under `workspace/images/case021` and masks under `workspace/masks/case021`.
