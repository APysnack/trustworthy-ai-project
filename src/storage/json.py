import json
import os


def save_json(results):
    os.makedirs("results", exist_ok=True)

    with open("results/results.json", "w") as file:
        json.dump(results, file, indent=2)