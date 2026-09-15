import os
import sys
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are Widget AI, a concise and sharp technical assistant.

Rules:
1. Give direct answers immediately in sentence 1. Never use greetings, filler, or intro setups (e.g., avoid "Hello", "Sure!", "Here is...").
2. Keep explanations high density and under 150 words.
3. Use bullet points for itemized details.
4. Format all code snippets in proper markdown code blocks with language names.
5. No concluding summaries or repetitive wrap-ups at the end.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(silent=True) or {}
        user_msg = data.get("message", "").strip()

        if not user_msg:
            return jsonify({"error": "Message cannot be empty."}), 400

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_msg}
            ],
            temperature=0.3,
            max_tokens=350
        )

        reply = completion.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        print(f"Groq API Error: {str(e)}", file=sys.stderr)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
