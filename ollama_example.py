import requests

def query_ollama(prompt):
    try:
        url = "http://localhost:11434/api/generate"

        payload = {
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(url, json=payload)

        data = response.json()
        return data.get("response", str(data))

    except Exception as e:
        return f"Error: {e}"
    
if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    print("Response:")
    print(query_ollama(prompt))