# Converter Recipe case003

## Goal
Prepare PNG image slices for case003 using repeatable settings.

## Commands
```bash
cd ~/git/nifti-image-converter
python3 python/nii2png.py \
  -i data/case003.nii.gz \
  -o workspace/images/case003 \
  --axis z \
  --rotate 180 \
  --normalize per-slice \
  --prefix case003 \
  --index-width 3 \
  --manifest-json workspace/images/case003-manifest.json \
  --yes
```

## Integration Notes
- Keep `--prefix`, `--axis`, and `--index-width` aligned with `lungmask` export settings.
- Keep images under `workspace/images/case003` and masks under `workspace/masks/case003`.
