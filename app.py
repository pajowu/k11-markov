from flask import Flask
from models import MODELS
import random
import json

app = Flask(__name__)

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader("./templates"),
    autoescape=select_autoescape(["html", "xml"]),
)

with open("data/cities.json") as f:
    CITIES = json.load(f)
with open("data/animals.json") as f:
    ANIMALS = json.load(f)

MODEL_NAMES = [(id, model["name"]) for id, model in MODELS.items()]
MODEL_NAMES.sort(key=lambda x: x[1])


@app.route("/")
def index():
    # sentence = model.make_sentence(tries=10000) or "Fehler! Bitte neuladen"
    # season = str(random.randint(1, 15))
    # episode = str(random.randint(1, 100))
    # return TEMPLATE.replace("%% SENTENCE %%",sentence).replace("%% EPISODE %%",episode).replace("%% SEASON %%", season)
    return str(MODELS.keys())


@app.route("/soko")
def soko():
    model = MODELS["soko"]
    template = env.get_template("soko.html")
    city = random.choice(CITIES)
    title = model["model"].make_sentence(tries=10000) or "Fehler! Bitte neuladen"
    return template.render(
        {"title": title, "city": city, "model": model, "models": MODEL_NAMES}
    )


@app.route("/tierpark")
def tierpark():
    model = MODELS["tierpark"]
    title = model["model"].make_sentence(tries=10000) or "Fehler! Bitte neuladen"
    animal1 = random.choice(ANIMALS)
    animal2 = random.choice(ANIMALS)
    template = env.get_template("tierpark.html")
    return template.render(
        {
            "title": title,
            "animal1": animal1,
            "animal2": animal2,
            "model": model,
            "models": MODEL_NAMES,
        }
    )


@app.route("/<model_name>")
def model(model_name):
    model = MODELS[model_name]
    title = model["model"].make_sentence(tries=10000) or "Fehler! Bitte neuladen"
    season = str(random.randint(1, 15))
    episode = str(random.randint(1, 100))
    template = env.get_template("generic_model.html")
    return template.render(
        {
            "title": title,
            "season": season,
            "episode": episode,
            "model": model,
            "models": MODEL_NAMES,
        }
    )
