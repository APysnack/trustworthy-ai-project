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
    if experiment.condition == "no_evidence":
        pass
    else:
        if not experiment.evidence:
            raise ValueError(
                f"Evidence is required for condition {experiment.condition}."
            )
        prompt += f"\n\nEvidence: {experiment.evidence}"

    return prompt
