from huggingface_hub import InferenceClient
import os

def query_huggingface(prompt):
    try:
        client = InferenceClient(
            model="HuggingFaceH4/zephyr-7b-beta",
            token=os.getenv("HUGGINGFACE_API_KEY")
        )

        response = client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    print("Response:")
    print(query_huggingface(prompt))