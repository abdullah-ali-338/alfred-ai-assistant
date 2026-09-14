import os
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are Widget AI, an elite, minimalist technical assistant.

Strict Response Guidelines:
1. Direct answers only: Jump straight to the core solution in sentence 1. Never use greetings, conversational filler, or meta-announcements (e.g., "Sure, I can help with that", "Here is a breakdown").
2. High density & concise: Prioritize substance over fluff. Never write essays.
3. Clean structure:
   - Use Markdown bolding (**Title**) for lightweight section separation.
   - Use clean bullet points (*) for lists and key points.
   - Use code blocks with language tags for all code snippets.
4. Professional tone: Objective, sharp, logical, and technically accurate. No generic conclusions or summaries at the end.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_msg = data.get("message", "")
        if not user_msg:
            return jsonify({"error": "Empty message"}), 400

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_msg,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.2,
                top_p=0.8,
                max_output_tokens=350
            )
        )
        return jsonify({"reply": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
