import markovify
import json
import argparse
from models import MODELS

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--model_name", required=True, choices=MODELS.keys())
	parser.add_argument("-n", type=int, default=10)
	parser.add_argument("--tries", type=int, default=1000)
	args = parser.parse_args()

	i=0
	while i < args.n:
		sentence = MODELS[args.model_name]['model'].make_sentence(tries=args.tries)
		print(sentence)

		i+=1
