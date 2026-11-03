from dataclasses import dataclass

from data import Question
from evidence import create_relevant_evidence, create_irrelevant_evidence, generate_conflicting_evidence


@dataclass
class Experiment:
    question: Question
    condition: str
    evidence: str | None
    conflict_answer: str | None = None # For seeing if LLM follows conflicting evidence or not

'''create the four conditions for each question'''
def create_experiments(
    question: Question,
    questions: list[Question]
) -> list[Experiment]:
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
        Experiment(
            question=question,
            condition="irrelevant_evidence",
            evidence=create_irrelevant_evidence(question, questions),
        ),
        Experiment(
            question=question,
            condition="conflicting_evidence",
            evidence=generate_conflicting_evidence(question)[0],
            conflict_answer=generate_conflicting_evidence(question)[1],
        ),
    ]

def create_all_experiments(questions):
    experiments = []

    for question in questions:
        experiments.extend(create_experiments(question, questions))

    return experiments