import re
import json
names = []

for line in open("input_raw.txt"):
	name = line.strip().strip("*")
	if m:= re.match(r'(.*) \((\d+)\)',name):
		name = m.group(1)

	if name not in names:
		names.append(name)

with open("input_cleaned.json", "w") as f:
	json.dump(names, f)
