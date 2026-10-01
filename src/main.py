import json
import os

from squad import SquadDataset
from llm import ask_llm


dataset = SquadDataset()

examples = dataset.get_range(0, 10)

results = []

for example in examples:

    response_without_context = ask_llm(example.question)

    response_with_context = ask_llm(
        example.question,
        example.context
    )

    results.append({
        "question": example.question,
        "answer": example.answer,
        "without_context": response_without_context,
        "with_context": response_with_context
    })


os.makedirs("results", exist_ok=True)

with open("results/results.json", "w") as file:
    json.dump(results, file, indent=2)