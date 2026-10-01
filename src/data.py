import json
from dataclasses import asdict, dataclass

from datasets import load_dataset


@dataclass
class Question:
    id: str
    title: str
    question: str
    correct_answer: str
    context: str


def load_squad():
    return load_dataset("rajpurkar/squad", split="train")


def select_questions(dataset, start, end):
    return dataset.select(range(start, end))


def format_question(item):
    return Question(
        id=item["id"],
        title=item["title"],
        question=item["question"],
        correct_answer=item["answers"]["text"][0],
        context=item["context"],
    )


def prepare_questions(start, end):
    dataset = load_squad()
    selected = select_questions(dataset, start, end)

    return [format_question(item) for item in selected]


def save_questions(questions, filename):
    with open(filename, "w") as file:
        json.dump([asdict(question) for question in questions], file, indent=2)