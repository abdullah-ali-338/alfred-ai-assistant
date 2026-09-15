# Widget AI

A lightweight, low-latency conversational assistant powered by Flask and Google's Gemini Flash model. Features a responsive, glassmorphic UI with light/dark theme support, dynamic Markdown rendering, and custom DNS integration.

**Live Demo:** [https://widget-ai.duckdns.org](https://widget-ai.duckdns.org)

---

## Features

- **LLM Core**: Google's Gemini Flash via the official `google-genai` SDK
- **Strict Response Framing**: Structured system rules for concise, high-density outputs
- **Modern UI**: Custom CSS with Plus Jakarta Sans, glassmorphism, responsive mobile layouts, and zero-dependency dark/light mode toggle
- **Rich Text Rendering**: Integrated `marked.js` for lists, bold emphasis, and formatted code blocks
- **Error Resilience**: Connection retry mechanisms and asynchronous fetch handling
- **Cloud Deployed**: Continuous deployment via Render with custom DNS routing over DuckDNS

---

## Tech Stack

| Layer | Technology |
| --- | --- |
| Backend | Python 3, Flask, Gunicorn |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| AI Integration | Google GenAI SDK |
| Formatting | Marked.js |
| Hosting | Render |
| DNS/Domain | DuckDNS |

---

## Project Structure

```
├── app.py              # Flask server, routes, Gemini SDK integration
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
└── templates/
    └── index.html      # Frontend interface, styles, client-side logic
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- Gemini API key from [Google AI Studio](https://aistudio.google.com/)

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/widget-ai.git
cd widget-ai
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_actual_api_key_here
PORT=5000
```

5. Start the application:
```bash
python app.py
```

Open `http://localhost:5000` in your browser.

---

## Deployment

### Render Setup

1. Connect your GitHub repository to Render as a Web Service
2. Set configuration:
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
3. Add environment variables:
   - `GEMINI_API_KEY` = your Google AI Studio key

### Custom Domain (DuckDNS)

1. Reserve a free subdomain at [DuckDNS](https://www.duckdns.org/)
2. Point the A Record to Render's routing IP:
```
216.24.57.1
```
3. Add your custom domain in Render Settings > Custom Domains for automatic SSL certificates

---

## License

This project is intended for educational and academic purposes.
