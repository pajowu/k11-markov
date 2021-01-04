import markovify
import re
import json

#nlp = spacy.load("de")

class POSifiedText(markovify.Text):
    # def word_split(self, sentence):
    #     return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

with open("model.json") as f:
	model = POSifiedText.from_json(json.load(f))
