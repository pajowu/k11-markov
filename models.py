import markovify
import json
from pathlib import Path

MODEL_PATH = Path("data/model")

MODEL_PATH.mkdir(exist_ok=True)

MODELS = {}
for file in MODEL_PATH.glob("*.json"):

    with open(file) as f:
        MODELS[file.stem] = json.load(f)

    MODELS[file.stem]['model'] = markovify.Text.from_dict(MODELS[file.stem]['model'])
