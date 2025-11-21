from model_conf import model

def generate_explanation(prompt):
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    prompt = "Explain the theory of relativity in simple terms."
    explanation = generate_explanation(prompt)
    print("Generated Explanation:")
    print(explanation)