from llm import ask_llm


def answer_with_no_evidence(example):
    return ask_llm(example.question)


def answer_with_relevant_evidence(example):
    return ask_llm(
        example.question,
        example.context
    )


def run_experiment(examples):
    results = []

    for example in examples:
        no_evidence = answer_with_no_evidence(example)
        relevant_evidence = answer_with_relevant_evidence(example)

        results.append({
            "question": example.question,
            "correct_answer": example.answer,
            "answer_with_no_evidence": no_evidence,
            "answer_with_relevant_evidence": relevant_evidence
        })

    return results