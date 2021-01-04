import markovify
import re
import spacy
import json

# nlp = spacy.load("de")

class POSifiedText(markovify.Text):
    pass
    # def word_split(self, sentence):
    #     return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    # def word_join(self, words):
    #     sentence = " ".join(word.split("::")[0] for word in words)
    #     return sentence

with open("input_cleaned.json") as f:
    corpus = json.load(f)

text_model = POSifiedText(corpus)
with open("model.json", "w") as f:
    json.dump(text_model.to_json(), f)
