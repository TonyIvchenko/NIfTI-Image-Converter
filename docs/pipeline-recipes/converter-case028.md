# Converter Recipe case028

## Goal
Prepare PNG image slices for case028 using repeatable settings.

## Commands
```bash
cd ~/git/nifti-image-converter
python3 python/nii2png.py \
  -i data/case028.nii.gz \
  -o workspace/images/case028 \
  --axis x \
  --rotate 270 \
  --normalize global \
  --prefix case028 \
  --index-width 3 \
  --manifest-json workspace/images/case028-manifest.json \
  --yes
```

## Integration Notes
- Keep `--prefix`, `--axis`, and `--index-width` aligned with `lungmask` export settings.
- Keep images under `workspace/images/case028` and masks under `workspace/masks/case028`.
