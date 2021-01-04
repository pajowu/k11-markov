import markovify
import re
import json

with open("input_cleaned.json") as f:
    corpus = json.load(f)

text_model = markovify.Text(corpus)
with open("model.json", "w") as f:
    json.dump(text_model.to_json(), f)
