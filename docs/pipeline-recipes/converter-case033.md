# Converter Recipe case033

## Goal
Prepare PNG image slices for case033 using repeatable settings.

## Commands
```bash
cd ~/git/nifti-image-converter
python3 python/nii2png.py \
  -i data/case033.nii.gz \
  -o workspace/images/case033 \
  --axis z \
  --rotate 0 \
  --normalize per-slice \
  --prefix case033 \
  --index-width 3 \
  --manifest-json workspace/images/case033-manifest.json \
  --yes
```

## Integration Notes
- Keep `--prefix`, `--axis`, and `--index-width` aligned with `lungmask` export settings.
- Keep images under `workspace/images/case033` and masks under `workspace/masks/case033`.
