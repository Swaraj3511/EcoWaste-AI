import argparse
from pathlib import Path
import webbrowser

ROOT = Path(__file__).resolve().parents[1]
DOWNLOADS = ROOT / "dataset" / "_downloads"

SOURCES = [
    ("Recyclable Waste Image Dataset",
     "https://data.mendeley.com/datasets/h5pxbsdz4m/1",
     "CC BY 4.0"),
    ("Custom Bangladeshi E-Waste Image Dataset",
     "https://data.mendeley.com/datasets/77383kmdnw/1",
     "CC BY 4.0"),
    ("Waste Classification Dataset",
     "https://data.mendeley.com/datasets/n3gtgm9jxj/3",
     "CC BY 4.0"),
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--open", action="store_true")
    args = parser.parse_args()

    DOWNLOADS.mkdir(parents=True, exist_ok=True)

    print("EcoWaste AI Dataset Downloader")
    print("The old downloader failed because Mendeley's API returned HTTP 401.")
    print("This version does NOT use that API and will not report fake success.")

    if args.open:
        for name, url, license_name in SOURCES:
            print(f"\nOpening: {name}")
            print(f"License: {license_name}")
            print(url)
            webbrowser.open(url)

        print("\nAfter downloading the published ZIP files, put them here:")
        print(DOWNLOADS)
        print("\nThen use DATASET_MAPPING.md to place images into the six folders.")
        return

    print("\nRun this first:")
    print("  python scripts\\download_dataset.py --open")
    print("\nThe publisher pages provide the official Download All button.")
    print("This avoids the Mendeley API 401 problem.")

if __name__ == "__main__":
    main()
