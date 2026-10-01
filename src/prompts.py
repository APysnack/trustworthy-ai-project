# TODO: Figure out prompt wording, llm should answer in few words to match SQuAD answer format 
def build_prompt(experiment):
    prompt = f"""Answer the following question.

Question: {experiment.question.question}"""

    if experiment.condition == "relevant_evidence":
        prompt += f"\n\nEvidence: {experiment.evidence}"
    elif experiment.condition != "no_evidence":
        raise ValueError(f"Unknown condition: {experiment.condition}")

    return prompt