from flask import Flask
from model import model
import random
app = Flask(__name__)

with open("template.html") as f:
	TEMPLATE = f.read()

@app.route('/')
def hello_world():
	sentence = model.make_sentence(tries=10000) or "Fehler! Bitte neuladen"
	season = str(random.randint(1, 15))
	episode = str(random.randint(1, 100))
	return TEMPLATE.replace("%% SENTENCE %%",sentence).replace("%% EPISODE %%",episode).replace("%% SEASON %%", season)
