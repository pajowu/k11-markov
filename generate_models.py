import markovify
import re
import json
import glob
from pathlib import Path
import argparse

INPUT_PATH = Path("data/input")
OUTPUT_PATH = Path("data/model")

def main(state_size):
	INPUT_PATH.mkdir(exist_ok=True)
	OUTPUT_PATH.mkdir(exist_ok=True)

	for file in INPUT_PATH.glob("*.json"):
	    print(f"Generating model for {file.name}")
	    with open(file) as f:
	        input = json.load(f)

	    text_model = markovify.Text(input["names"], state_size=state_size)

	    output_dict = input
	    output_dict['model'] = text_model.to_dict()
	    with open(OUTPUT_PATH / file.name, "w") as f:
	        json.dump(output_dict, f, indent=4)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--state-size", type=int, default=1)
	args = parser.parse_args()

	main(args.state_size)
