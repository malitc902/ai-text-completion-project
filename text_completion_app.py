import os
import cohere

# Securely retrieve API key from environment variable
cohere_api_key = "c5shsfP2T5NHnUl2FeyMExRG3HjqvYXovuUJyB1h"

# Validate API key
if not cohere_api_key:
    raise ValueError("Error: API key is missing. Set COHERE_API_KEY as an environment variable.")

# Initialize Cohere client
co = cohere.Client(cohere_api_key)

def complete_text(prompt, model="command", max_tokens=800, temperature=0.7):
    """
    Function to generate text using Cohere API.
    
    Parameters:
    - prompt (str): The user input text.
    - model (str): Cohere model to use (default: 'command').
    - max_tokens (int): Max length of generated response.
    - temperature (float): Controls randomness in generation.
    
    Returns:
    - str: AI-generated response.
    """
    try:
        if not prompt.strip():
            return "Error: Please enter a valid prompt."
        
        response = co.generate(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )

        return response.generations[0].text  # Extract AI-generated text
    except cohere.CohereError as e:
        return f"API Error: {e.message}"  # Improved error handling

# Interactive loop for multiple requests
while True:
    user_input = input("\nEnter a prompt (or type 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    print("\nAI Response:", complete_text(user_input))