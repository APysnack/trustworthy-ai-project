from google import genai


client = genai.Client()


def ask_llm(question, context=None):
    prompt = f"Answer this question:\n\n{question}"

    if context:
        prompt += f"\n\nEvidence:\n{context}"

    interaction = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input=prompt,
        generation_config={
            "thinking_level": "low"
        }
    )

    return interaction.output_text