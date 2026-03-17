from google import genai
import os

# Initialize client with API key
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def query_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Response:")
    print(query_gemini(user_prompt))