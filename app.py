import os
from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Key system environment se load hogi, hardcoded nahi hai
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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
            model="gemini-3.6-flash",
            contents=user_msg
        )
        return jsonify({"reply": response.text})

    except Exception as e:
        print("Backend Error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
