import markovify
import re
import json

with open("model.json") as f:
	model = markovify.Text.from_json(json.load(f))
