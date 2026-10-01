from llm import ask_llm


def run_experiment(examples):
    results = []

    for example in examples:

        response_without_context = ask_llm(example.question)

        response_with_context = ask_llm(
            example.question,
            example.context
        )

        results.append({
            "question": example.question,
            "correct_answer": example.answer,
            "answer_with_no_evidence": response_without_context,
            "answer_with_evidence": response_with_context
        })

    return results