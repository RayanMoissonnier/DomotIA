import ollama

# Choisissez le modèle installé (ex: 'llama2', 'llama3', 'mistral')
model_name = "llama3"

# On commence la conversation avec un message système (optionnel)
messages = [
    {
        "role": "system",
        "content": "Tu es un assistant IA. Tu dois TOUJOURS répondre uniquement en français, même si la question est posée dans une autre langue.",
    }
]

print("Chatbot Ollama (tapez Entrée sans texte pour quitter)")

while True:
    user_input = input("Vous : ")
    if not user_input:
        break
    messages.append({"role": "user", "content": user_input})
    response = ollama.chat(model=model_name, messages=messages)
    answer = response.message.content
    print("Bot :", answer)
    messages.append({"role": "assistant", "content": answer})
