from google import genai

from data import prepare_questions
from experiment import create_all_experiments
from generation import generate_responses
from evaluation import evaluate_results
from results import save_results


def main():
    client = genai.Client()

    questions = prepare_questions(0, 5)

    experiments = create_all_experiments(questions)

    responses = generate_responses(client, experiments)

    evaluated_results = evaluate_results(responses)

    save_results(evaluated_results, "results/results.json")

    for result in evaluated_results:
        print(f"Condition: {result['condition']}")
        print(f"Question: {result['question']}")
        print(f"Correct answer: {result['correct_answer']}")
        print(f"Model response: {result['response']}")
        print(f"Correct: {result['correct']}")
        print()


if __name__ == "__main__":
    main()