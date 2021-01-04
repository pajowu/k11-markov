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
	reconstituted_model = POSifiedText.from_json(json.load(f))

with open("input_cleaned.json") as f:
	input = json.load(f)

i = 0
dups = 0
sentences = set()
while i < 10000:
	sentence = reconstituted_model.make_sentence(tries=1000)
	if sentence in input:
		print("In Input", i, sentence)


	if sentence in sentences:
		print("Duplicate", i, sentence)
		dups += 1
	sentences.add(sentence)
	i += 1

print(dups / i * 100)
