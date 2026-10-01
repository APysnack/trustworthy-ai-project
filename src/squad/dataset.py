from dataclasses import dataclass

from datasets import load_dataset


@dataclass
class SquadExample:
    id: str
    title: str
    context: str
    question: str
    answer: str


class SquadDataset:
    def __init__(self):
        dataset = load_dataset("rajpurkar/squad", split="train")

        self.examples = []

        for item in dataset:
            example = SquadExample(
                id=item["id"],
                title=item["title"],
                context=item["context"],
                question=item["question"],
                answer=item["answers"]["text"][0],
            )

            self.examples.append(example)

    def get_range(self, start, end):
        return self.examples[start:end]