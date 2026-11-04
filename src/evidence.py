from data import Question
import re

def create_relevant_evidence(question: Question):
    return question.context

''' find candidate contexts from related questions'''
def find_related_contexts(
    question: Question,
    questions: list[Question]
) -> list[Question]:
    # Initialize an empty list of candidate questions.
    candidates = []
    print(
        f"[DEBUG] Finding irrelevant evidence for question {question.id}: "
        f"title={question.title!r}, answer={question.correct_answer!r}, "
        f"context_length={len(question.context)}"
    )

    for candidate in questions:
        # Skip the target question itself (matching ID).
        if candidate.id == question.id:
            print(f"[DEBUG] Candidate {candidate.id}: rejected (same question)")
            continue

        # Skip candidates from a different article (different title).
        if candidate.title != question.title:
            print(
                f"[DEBUG] Candidate {candidate.id}: rejected (different title; "
                f"title={candidate.title!r})"
            )
            continue

        # Skip candidates that share the target's exact context.
        if candidate.context == question.context:
            print(f"[DEBUG] Candidate {candidate.id}: rejected (same context)")
            continue

        # Skip candidates with empty question text or context.
        if not candidate.question.strip() or not candidate.context.strip():
            print(
                f"[DEBUG] Candidate {candidate.id}: rejected (empty question "
                f"or context; question_length={len(candidate.question)}, "
                f"context_length={len(candidate.context)})"
            )
            continue

        # Skip candidates whose context contains the target's correct answer,
        # using normalized, contiguous token matching.
        answer_tokens = re.findall(r"\w+", question.correct_answer.lower())
        context_tokens = re.findall(r"\w+", candidate.context.lower())

        answer_length = len(answer_tokens)
        contains_answer = any(
            context_tokens[i:i + answer_length] == answer_tokens
            for i in range(len(context_tokens) - answer_length + 1)
        )

        if contains_answer:
            print(
                f"[DEBUG] Candidate {candidate.id}: rejected (context contains "
                f"answer tokens {answer_tokens!r})"
            )
            continue

        # Add the remaining candidate Question object to the list.
        candidates.append(candidate)
        print(
            f"[DEBUG] Candidate {candidate.id}: accepted "
            f"(context_length={len(candidate.context)})"
        )

    # Return the eligible candidates.
    # Return [] if no eligible candidates exist.
    print(f"[DEBUG] Eligible irrelevant evidence candidates: {len(candidates)}")
    return candidates

'''construct/filter related-but-irrelevant evidence'''
def create_irrelevant_evidence(
    question: Question,
    questions: list[Question]
) -> str:
    # Call find_related_contexts.
    candidates = find_related_contexts(question, questions)

    # Raise ValueError with target question ID if no candidates.
    if not candidates:
        raise ValueError(
            f"No eligible irrelevant evidence found for question {question.id}."
        )

    # Select first candidate deterministically.
    candidate = candidates[0]

    # Return candidate.context.
    return candidate.context


# def generate_conflicting_evidence(question: Question)-> tuple[str, str]:
#     # Generate a passage that contradicts the correct answer.
#     # Generate or extract the alternative answer supported by that passage.
#     # Return both the passage and alternative answer.


# def validate_conflicting_evidence(
#     question: Question,
#     evidence: str,
#     conflict_answer: str
# ) -> bool:
#     # Reject empty evidence or an empty alternative answer.
#     # Reject an alternative answer that matches question.correct_answer
#     # after normalization.
#     # Check that the passage supports conflict_answer.
#     # Check that the passage contradicts question.correct_answer.
#     # Return True only if all checks pass.