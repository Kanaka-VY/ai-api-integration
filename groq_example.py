import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def query_groq(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    print("Response:")
    print(query_groq(prompt))