import argparse
import json
from pathlib import Path


def combine(input, output, name):
    output_data = {"name": name, "names": [], "sources": []}
    for file in input:
        with open(file) as f:
            input_data = json.load(f)

        if "license_name" in input_data:
            if "license_name" not in output_data:
                output_data["license_name"] = input_data["license_name"]

            else:
                assert (
                    output_data.get("license_name") == input_data.get("license_name")
                ), "Input files with different license names provided. This is not supported"

        if "license_url" in input_data:
            if "license_url" not in output_data:
                output_data["license_url"] = input_data["license_url"]

            else:
                assert (
                    output_data.get("license_url") == input_data.get("license_url")
                ), "Input files with different license urls provided. This is not supported"

        if "sources" in input_data:
            for source in input_data['sources']:
                if source not in output_data['sources']:
                    output_data['sources'].append(source)

        for title in input_data["names"]:
            if title not in output_data["names"]:
                output_data["names"].append(title)

    with open(output, "w") as f:
        json.dump(output_data, f, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="append", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--name", required=True)

    args = parser.parse_args()

    combine(args.input, args.output, args.name)
