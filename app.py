import os
import sys
from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

INSTRUCTIONS = """
You are Widget AI. Follow these rules strictly:
- Give direct, crisp, and high-value answers.
- Jump straight to the point in the first sentence. No greetings or pleasantries like 'Sure', 'Hello', or 'Here is...'.
- Use short bullet points for lists.
- Keep the overall response brief and under 150 words unless writing code.
- Format all code in proper markdown code blocks.
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

        formatted_prompt = f"{INSTRUCTIONS}\n\nUser Question: {user_msg}\nWidget AI Response:"

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=formatted_prompt
        )

        return jsonify({"reply": response.text})

    except Exception as e:
        print(f"Server Error: {str(e)}", file=sys.stderr)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
