# Converter Recipe case034

## Goal
Prepare PNG image slices for case034 using repeatable settings.

## Commands
```bash
cd ~/git/nifti-image-converter
python3 python/nii2png.py \
  -i data/case034.nii.gz \
  -o workspace/images/case034 \
  --axis x \
  --rotate 90 \
  --normalize global \
  --prefix case034 \
  --index-width 3 \
  --manifest-json workspace/images/case034-manifest.json \
  --yes
```

## Integration Notes
- Keep `--prefix`, `--axis`, and `--index-width` aligned with `lungmask` export settings.
- Keep images under `workspace/images/case034` and masks under `workspace/masks/case034`.
