# EcoWaste AI — Fixed Complete Repo

Prepared for `Swaraj3511`.

## Fix for the HTTP 401 problem

The previous script called a Mendeley API endpoint and received:

```text
HTTP Error 401: Unauthorized
```

This version does not call that API.

## Dataset download

Run:

```bat
python scripts\download_dataset.py --open
```

The official publisher pages will open in your browser.

Use their **Download All** button and save the ZIP files into:

```text
dataset/_downloads/
```

Then organize the images according to `DATASET_MAPPING.md`.

## Six project classes

- plastic
- paper
- metal
- organic
- glass
- e-waste

## Object detection

The website can draw boxes using a browser detector, but a genuine custom six-class detector requires annotated bounding boxes and a trained model. The `model/` directory is intentionally ready for the exported custom model.
