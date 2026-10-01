from google.genai import types

from prompts import build_prompt


MODEL = "gemini-3.1-flash-lite"


def generate_response(client, prompt):
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                thinking_level="low"
            )
        ),
    )

    return response.text


def generate_responses(client, experiments):
    responses = []

    for experiment in experiments:
        prompt = build_prompt(experiment)
        response = generate_response(client, prompt)

        responses.append({
            "question_id": experiment.question.id,
            "condition": experiment.condition,
            "question": experiment.question.question,
            "correct_answer": experiment.question.correct_answer,
            "evidence": experiment.evidence,
            "response": response,
        })

    return responses


def handle_api_error(error):
    pass