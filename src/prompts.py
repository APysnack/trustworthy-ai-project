from experiment import Experiment

# TODO: Figure out prompt wording, llm should answer in few words to match SQuAD answer format 
'''construct the prompt for a question/condition
Keep the four conditions as consistent as possible while varying the evidence'''
def build_prompt(experiment: Experiment) -> str:
    prompt = f"""Answer the following question.

Question: {experiment.question.question}"""

    # If condition == "no_evidence":
        #   Do not include an evidence section.
    # Otherwise:
        #   Check that experiment.evidence is not empty.
        #   Include experiment.evidence in the prompt.
    if experiment.condition == "relevant_evidence":
        prompt += f"\n\nEvidence: {experiment.evidence}"
    elif experiment.condition != "no_evidence":
        raise ValueError(f"Unknown condition: {experiment.condition}")

    return prompt
