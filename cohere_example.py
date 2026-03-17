import os
import cohere

# Create client
co = cohere.ClientV2(os.getenv("COHERE_API_KEY"))

def query_cohere(prompt):
    try:
        response = co.chat(
            model="command-r7b-12-2024",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.message.content[0].text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Response:")
    print(query_cohere(user_prompt))