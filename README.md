# k11-markov

Ein Webservice, der neue Episodentitel für Fernsehserien generiert

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

### Generating data

Do train a model, you need data.
One good source is wikipedia.
One script to generate data from wikipedia is provided as `get_data_wikipedia.py`.

#### Manually collected data

You can also use data you collected manually.
Put the episode names in a text file. One per line.
An example file is given as `example_input.txt`.
`clean.py` can clean up the names by removing trailing `*` characters and numbers for multi-episodes.
It does the second by looking for names that end in ` (NUMBER)` then removes that part.

Running

```
python clean.py --input INPUT_FILE --output OUTPUT_FILE --name SERIES_NAME
```

creates a new json-file `OUTPUT_FILE`.
You can also pass a license name and url, for example `--license_name "CC-BY-SA" --license_url "https://creativecommons.org/licenses/by-sa/3.0/legalcode"`
You can also pass a source name and url, for example `--source_name "Wikipedia" --source_url "https://de.wikipedia.org/wiki/K11_%E2%80%93_Kommissare_im_Einsatz/Episodenliste"` for content from wikipedia.

To train the model, store the json-file from the last step in the `data/input` directory.

### Training the models

The file(s) in `data/input` can now be used to generate a model.
Now you can train the model by running

```
python generate_models.py
```

You can optionally pass the `--state-size` option to change the state size of the generated markov chain.
This creates new files with the same name in `data/models` with your models.

### Evaluating the Models

After generating the model it is interesting to check how good the generated titles are.
Two scripts are provided for that: `generate_sentences.py` and `measure_models.py`.

`generate_sentences.py` is interesting to get a quick look on how good the generated title are.
You start it by running

```
python generate_sentences.py --model_name MODEL_NAME
```

Which will generate 10 sentences by default.
Use the `--help` option to get a list of all option.


`measure_models.py` runs over all models and tries to generate a large number of sentences (10k by default).
It then looks at the generated sentences and counts how often the generation succeeds and how often the sentences repeat.

If `generate_sentences.py` gives you a lot of weird and grammatically wrong sentences, try using a bigger `--state-size`.
If `measure_models.py` reports a high number of duplicates, try using a smaller `--state-size`.

### Combining input data

Sometimes you might wish to combine different input files. For example all true crime series.
For that, `combine_input.py` is provided.
To use it, pass all input files to the `--input` parameter, the output file to the `--output` parameter and the name of the generated series to the `--name` parameter.
**NOTE**: Only input files with the same license can be combined

```
python combine_input.py --input INPUT1 --input INPUT2 --output data/input/OUTPUT.json --name OUTPUT_NAME
```

You need to regenerate the models afterwards.

## Deployment

`systemd/` contains systemd units for deploying this code.
They are based on the [gunicorn documentation](https://docs.gunicorn.org/en/stable/deploy.html#nginx-configuration), which you can see for more detailed instructions.

## LICENSE

This code is licensed under an AGPL-3.0 with the exception for `example_input.txt`.
These files are based on [Wikipedia](https://de.wikipedia.org/wiki/K11_%E2%80%93_Kommissare_im_Einsatz/Episodenliste) and are therefore under a [CC-BY-SA](https://creativecommons.org/licenses/by-sa/3.0/legalcode)
