from openai import OpenAI
from transformers import pipeline

def generate_code(prompt, api_key=None):
    try:
        if api_key:
            # Use OpenAI API if key provided
            client = OpenAI(api_key=api_key)
            response = client.completions.create(
                model="code-davinci-002",
                prompt=prompt,
                max_tokens=200
            )
            return response.choices[0].text
        else:
            # Fallback to HuggingFace
            generator = pipeline("text-generation", model="Salesforce/codegen-350M-multi")
            return generator(prompt, max_length=200)[0]['generated_text']
    except Exception as e:
        return f"Code generation failed: {e}"