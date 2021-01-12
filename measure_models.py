import markovify
import json
from models import MODELS


def measure_model(model, n=1000, tries=1000):
    i = 0
    dups = 0
    unsuccessful = 0
    sentences = set()
    while i < n:
        sentence = model["model"].make_sentence(tries=tries, max_overlap_ratio=95)
        if sentence == None:
            unsuccessful += 1

        elif sentence in sentences:
            dups += 1
        sentences.add(sentence)
        i += 1

    return n, dups, unsuccessful, tries


for model_id, model in MODELS.items():
    print(f"Measuring {model_id}...")
    n, dups, unsuccessful, tries = measure_model(model, n=10000)
    print(f"---------------------- {model['name']} ----------------------")
    print(f"Tried to generate {n} sentences with {tries} tries.")
    print(f"Failed to generate: {unsuccessful} ({unsuccessful / n * 100}%)")
    print(f"Generated duplicate: {dups} ({dups / n * 100}%)")
    print(f"Generated {n - dups - unsuccessful} unique sentences")
