import json


def save_results(results, filename):
    with open(filename, "w") as file:
        json.dump(results, file, indent=2)