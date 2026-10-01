from dataclasses import dataclass

from data import Question
from evidence import create_relevant_evidence


@dataclass
class Experiment:
    question: Question
    condition: str
    evidence: str | None


def create_experiments(question):
    return [
        Experiment(
            question=question,
            condition="no_evidence",
            evidence=None,
        ),
        Experiment(
            question=question,
            condition="relevant_evidence",
            evidence=create_relevant_evidence(question),
        ),
    ]

def create_all_experiments(questions):
    experiments = []

    for question in questions:
        experiments.extend(create_experiments(question))

    return experiments