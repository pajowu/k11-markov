# k11-markov

Ein Webservice, der neue Episodentitel für die SAT.1-Fernsehserie [„K11 – Kommissare im Einsatz“](https://de.wikipedia.org/wiki/K11_–_Kommissare_im_Einsatz) generiert.

## Installation

Install python 3. Run the following to install the necessary requirements:

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Usage

To run the webserver, simply run

```
gunicorn -b localhost:8000 app:app
```

After that visit [http://localhost:8000](http://localhost:8000).

## Training your own model

Put the episode names in `input_raw.txt`. One per line.
`clean.py` can clean up the names by removing trailing `*` characters and numbers for multi-episodes.
It does the second by looking for names that end in ` (NUMBER)` then removes that part.

Running

```
python clean.py
```

creates a new file called `input_cleaned.json`.

This file can now be used to generate a model.
Now you can train the model by running.

```
python generate_model.py
```

This create a new `model.json` with you model.

## LICENSE

This code is licensed under an AGPL-3.0 with the exception fo the `input_raw.txt`, `input_cleaned.json` and `model.json`.
These files are based on [Wikipedia](https://de.wikipedia.org/wiki/K11_%E2%80%93_Kommissare_im_Einsatz/Episodenliste) and are therefore under a [CC-BY-SA](https://creativecommons.org/licenses/by-sa/3.0/legalcode)
