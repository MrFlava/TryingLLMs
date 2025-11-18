from model_conf import model

# Generate content
prompt = "Explain the concept of quantum entanglement in simple terms."
response = model.generate_content(prompt)

# Print the generated text
print(response.text)