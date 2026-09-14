import os
import sys
from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = (
    "You are Widget AI, a concise and direct technical assistant. "
    "Give sharp, clear answers. Avoid introductory greetings, filler, or fluff. "
    "Use bullet points for lists and code blocks where applicable."
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(silent=True) or {}
        user_msg = data.get("message", "").strip()
        
        if not user_msg:
            return jsonify({"error": "Message is empty"}), 400
           
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_msg}\nAssistant:"

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=full_prompt
        )

        return jsonify({"reply": response.text})

    except Exception as e:
        print(f"Error occurred: {str(e)}", file=sys.stderr)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
