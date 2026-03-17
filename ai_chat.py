import ollama

print("Local AI Chatbot (type 'exit' to stop)")

messages = []

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    messages.append({"role": "user", "content": user})

    response = ollama.chat(
        model="gemma3:1b",
        messages=messages
    )

    ai_reply = response["message"]["content"]

    print("AI:", ai_reply)

    messages.append({"role": "assistant", "content": ai_reply})