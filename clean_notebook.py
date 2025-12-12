import json
import sys

def clean_notebook(path):
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    if "metadata" in nb and "widgets" in nb["metadata"]:
        del nb["metadata"]["widgets"]
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=2)
        print(f"✅ Cleaned widgets metadata: {path}")
    else:
        print("No widgets metadata found — nothing to do.")

if __name__ == "__main__":
    for p in sys.argv[1:]:
        clean_notebook(p)