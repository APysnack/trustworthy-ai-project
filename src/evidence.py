from data import Question

def create_relevant_evidence(question: Question):
    return question.context

''' find candidate contexts from related questions'''
def find_related_contexts(
    question: Question,
    questions: list[Question]
) -> list[Question]:
    # Initialize an empty list of candidate questions.

    for candidate in questions:
        # Skip the target question itself (matching ID).
        # Skip candidates from a different article (different title).
        # Skip candidates that share the target's exact context.
        # Skip candidates with empty question text or context.
        # Skip candidates whose context contains the target's correct answer,
        # using normalized, contiguous token matching.

        # Add the remaining candidate Question object to the list.

    # Return the eligible candidates.
    # Return [] if no eligible candidates exist.

'''construct/filter related-but-irrelevant evidence'''
def create_irrelevant_evidence(
    question: Question,
    questions: list[Question]
) -> str:
    # Call find_related_contexts() to get eligible Question objects.
    # If no candidates exist, raise ValueError with the target question ID.
    # Select one candidate (e.g., the first candidate).
    # Return candidate.context as a string.


def generate_conflicting_evidence(question: Question)-> tuple[str, str]:
    # Generate a passage that contradicts the correct answer.
    # Generate or extract the alternative answer supported by that passage.
    # Return both the passage and alternative answer.


def validate_conflicting_evidence(
    question: Question,
    evidence: str,
    conflict_answer: str
) -> bool:
    # Reject empty evidence or an empty alternative answer.
    # Reject an alternative answer that matches question.correct_answer
    # after normalization.
    # Check that the passage supports conflict_answer.
    # Check that the passage contradicts question.correct_answer.
    # Return True only if all checks pass.