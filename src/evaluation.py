# TODO: atm it just checks if the response is exactly equal to the answer which will be false
def evaluate_accuracy(response, correct_answer):
    return response == correct_answer


def evaluate_results(responses):
    for result in responses:
        result["correct"] = evaluate_accuracy(
            result["response"],
            result["correct_answer"],
        )

    return responses