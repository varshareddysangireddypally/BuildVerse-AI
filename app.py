
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import json

app = Flask(__name__, static_folder="frontend")
CORS(app)

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:3b"


def ask_ollama(messages, json_mode=False):
    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }

    if json_mode:
        payload["format"] = "json"

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=180
    )
    response.raise_for_status()

    return response.json()["message"]["content"]


@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")


# Original code-explanation endpoint
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True) or {}
    code = data.get("code", "").strip()

    if not code:
        return jsonify({
            "error": "Please enter code or an error message."
        }), 400

    try:
        answer = ask_ollama([
            {
                "role": "system",
                "content": (
                    "You are a beginner-friendly coding assistant. "
                    "Explain code in simple language, identify likely "
                    "errors, and suggest debugging steps. Never claim "
                    "that you executed or tested code."
                )
            },
            {"role": "user", "content": code}
        ])

        return jsonify({"result": answer})

    except requests.exceptions.RequestException:
        app.logger.exception("Ollama request failed")
        return jsonify({
            "error": "Could not connect to the local AI model."
        }), 503


# BuildVerse AI roadmap endpoint
@app.route("/api/roadmap", methods=["POST"])
def roadmap():
    idea = request.form.get("idea", "").strip()
    level = request.form.get("level", "Beginner")
    technology = request.form.get(
        "technology", "Recommend for me"
    )

    if not idea:
        return jsonify({
            "error": (
                "Please describe your project idea in text. "
                "Image preview is supported, but image analysis "
                "is not configured in this version."
            )
        }), 400

    allowed_levels = ["Beginner", "Intermediate", "Advanced"]
    allowed_technologies = [
        "Recommend for me", "Python", "JavaScript", "Java"
    ]

    if level not in allowed_levels:
        level = "Beginner"

    if technology not in allowed_technologies:
        technology = "Recommend for me"

    prompt = f"""
Create a realistic software project roadmap.

PROJECT IDEA:
{idea}

USER EXPERIENCE:
{level}

USER TECHNOLOGY PREFERENCE:
{technology}

TECHNOLOGY RULES:
1. Respect the user's selected technology.
2. If the user selects Python, prefer Python with Flask
   or another suitable Python framework.
3. If the user selects JavaScript, prefer HTML, CSS,
   JavaScript and, only if needed, Node.js.
4. If the user selects Java, prefer Java with a suitable
   framework such as Spring Boot when appropriate.
5. If the user selects Recommend for me, choose a simple,
   suitable stack based on the project idea.
6. For beginners, prefer a small working prototype,
   simple tools, and a manageable database such as SQLite.
7. Do not recommend React Native, Firebase, cloud services,
   or paid APIs unless the project actually needs them.
8. Do not add facial recognition or other advanced AI
   features unless relevant to the idea. If advanced,
   describe them as optional future enhancements.
9. Include only tools needed for this project. Briefly
   explain why each technology is useful.
10. Make tasks specific, practical, and non-repetitive.
11. Estimated hours must be numbers, not text.
12. Do not claim that a suggested feature is already built.

Return valid JSON only in this structure:
{{
  "project_summary": "Short project description",
  "detected_features": [
    "Relevant feature 1",
    "Relevant feature 2"
  ],
  "tech_stack": [
    "Technology - why it is suitable"
  ],
  "phases": [
    {{
      "title": "Phase title",
      "estimated_hours": 4,
      "tasks": [
        "Specific task 1",
        "Specific task 2"
      ]
    }}
  ],
  "risks": [
    "Potential risk and a practical way to reduce it"
  ]
}}

Create 3 to 5 phases. Make the roadmap suitable for the
user's experience level. Keep the first version achievable.
Return no Markdown fences or extra text.
"""

    try:
        answer = ask_ollama([
            {
                "role": "system",
                "content": (
                    "You are BuildVerse AI, a beginner-friendly "
                    "software project planning assistant. Follow "
                    "the user's preferences and return valid JSON "
                    "with the exact requested keys."
                )
            },
            {"role": "user", "content": prompt}
        ], json_mode=True)

        data = json.loads(answer)

        required = [
            "project_summary",
            "detected_features",
            "tech_stack",
            "phases",
            "risks"
        ]

        if not all(key in data for key in required):
            raise ValueError("The AI response is missing fields.")

        # Remove repeated tasks on the backend too.
        seen = set()

        for phase in data["phases"]:
            cleaned_tasks = []

            for task in phase.get("tasks", []):
                task_text = str(task).strip()
                task_key = task_text.casefold()

                if task_text and task_key not in seen:
                    seen.add(task_key)
                    cleaned_tasks.append(task_text)

            phase["tasks"] = cleaned_tasks

        return jsonify(data)

    except requests.exceptions.Timeout:
        return jsonify({
            "error": "The AI took too long. Please try again."
        }), 504

    except requests.exceptions.RequestException:
        app.logger.exception("Ollama request failed")
        return jsonify({
            "error": (
                "Could not connect to Ollama. Check that it is running."
            )
        }), 503

    except (ValueError, KeyError, TypeError):
        app.logger.exception("Invalid roadmap response")
        return jsonify({
            "error": "The AI returned an invalid roadmap. Please try again."
        }), 502


if __name__ == "__main__":
    app.run(debug=True, port=5000)
