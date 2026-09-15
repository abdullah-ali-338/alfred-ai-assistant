# Widget AI

A lightweight, low-latency conversational assistant powered by Flask and Groq's high-speed inference engine. Features a responsive glassmorphic UI, zero-dependency theme switching, dynamic Markdown rendering, and custom DNS integration.

**Live Demo:** https://widget-ai.duckdns.org

---

## Features

- **High-Speed Inference**: Open-weights models on Groq for sub-second token generation
- **Deterministic Responses**: Structured system prompts for direct, fluff-free explanations
- **Modern Interface**: Custom CSS with Plus Jakarta Sans, glassmorphism, responsive mobile views, and theme toggling
- **Native Markdown**: Marked.js integration for formatted lists, bold text, and code blocks
- **Automated Cloud Hosting**: Deployed on Render with custom DNS routing via DuckDNS

---

## Tech Stack

| Layer | Technology |
| --- | --- |
| Backend | Python 3, Flask |
| LLM Provider | Groq Cloud SDK |
| Frontend | Vanilla HTML5, CSS3, JavaScript |
| Parser | Marked.js |
| Deployment | Render |
| DNS | DuckDNS |

---

## Project Structure

```
├── app.py              # Flask server and Groq API implementation
├── requirements.txt    # Production dependencies
├── .env                # Environment configuration
└── templates/
    └── index.html      # Glassmorphic UI and client-side logic
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- Groq API Key from [console.groq.com](https://console.groq.com)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/widget-ai.git
cd widget-ai
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables in `.env`:
```
GROQ_API_KEY=your_groq_api_key_here
PORT=5000
```

5. Run the server:
```bash
python app.py
```

Open `http://localhost:5000` in your browser.

---

## Deployment

### Render Configuration

1. Create a New Web Service connected to your repository
2. Build Command: `pip install -r requirements.txt`
3. Start Command: `python app.py`
4. Add environment variable:
   - Key: `GROQ_API_KEY`
   - Value: your Groq API key

### Custom Domain (DuckDNS)

1. Create a subdomain on [DuckDNS](https://www.duckdns.org/)
2. Map your DuckDNS domain to Render IP:
```
216.24.57.1
```
3. Add the domain in Render dashboard under Settings > Custom Domains

---

## License

This project is licensed for educational and personal purposes.
