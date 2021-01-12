import re
import json
import argparse
from pathlib import Path


def clean(input, output, more_data):
    names = []

    for line in open(input):
        name = line.strip().strip("*")
        if m := re.match(r"(.*) \((\d+)\)", name):
            name = m.group(1)

        if name not in names:
            names.append(name)

    more_data["names"] = names

    with open(output, "w") as f:
        json.dump(more_data, f, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--name", required=True)
    parser.add_argument("--license_url")
    parser.add_argument("--license_name")
    parser.add_argument("--source_url")
    parser.add_argument("--source_name")

    args = parser.parse_args()

    more_data = {"name": args.name, "sources": []}

    if args.license_name:
        more_data["license_name"] = args.license_name

    if args.license_url:
        more_data["license_url"] = args.license_url

    if args.source_name or args.source_url:
        more_data["sources"].append({})

    if args.source_name:
        more_data["sources"][-1]["name"] = args.source_name

    if args.source_url:
        more_data["sources"][-1]["url"] = args.source_url

    clean(args.input, args.output, more_data)
