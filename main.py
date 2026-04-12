from flask import Flask, request, jsonify, render_template
from openai import OpenAI

# Hardcoded key for now (we'll secure later)

client = OpenAI(api_key=api_key)

app = Flask(__name__)

conversation = [
    {"role": "system", "content": "You are a futuristic AI hologram assistant."}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation
    )

    reply = response.choices[0].message.content
    conversation.append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)