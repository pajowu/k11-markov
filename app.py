import json
import random
from urllib.parse import urlparse

from flask import Flask, redirect, request
from jinja2 import Environment, FileSystemLoader, select_autoescape
from models import MODELS
from werkzeug.routing import BaseConverter, ValidationError

app = Flask(__name__)


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


class ModelNameConverter(BaseConverter):
    def to_python(self, value):
        if value not in MODELS:
            raise ValidationError()
        return value

    def to_url(self, value):
        return value


app.url_map.converters["model_name"] = ModelNameConverter


@app.route("/")
def index():
    o = urlparse(request.base_url)
    host = o.hostname
    if host.startswith("k11"):
        return redirect("/k11")
    else:
        return redirect("/tierpark")


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


@app.route("/<model_name:model_name>")
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
