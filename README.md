# 🚀 BuildVerse AI
### Turn Your Project Idea Into a Realistic Development Roadmap

<p align="center">
  <strong>Think it. Plan it. Build it.</strong>
</p>

<p align="center">
  An AI-powered project planning assistant that helps students and beginner developers transform project ideas into structured, actionable development roadmaps.
</p>

---

## 🌟 About the Project

Have a great software project idea but don't know where to start, which technologies to choose, or how to divide the work into manageable steps?

**BuildVerse AI is here to help!**

BuildVerse AI takes a project idea in plain English and uses a locally running AI model to generate a structured development plan. It helps beginners understand what to build, which tools may be suitable, what tasks to complete, and what challenges to consider before development begins.

Our goal is to make software project planning simpler, more accessible, and less overwhelming.

## ✨ Key Features

- 💡 **AI-Powered Project Understanding** — Generate a concise summary and identify relevant features from a project description.
- 🗺️ **Smart Roadmap Generation** — Break a project into organized development phases.
- ✅ **Task-Based Planning** — Get actionable tasks and track progress using a checklist.
- 🛠️ **Technology Recommendations** — Receive suggested tools and technologies suited to the project.
- ⏱️ **Time Estimation** — View estimated hours for development phases.
- ⚠️ **Risk Awareness** — Identify potential project risks and practical mitigation strategies.
- 🎯 **Beginner-Friendly Planning** — Generate roadmaps based on the selected experience level.
- 🔒 **Local AI Inference** — Use Ollama with Qwen 2.5 3B to generate roadmaps locally, without depending on a paid cloud AI inference API.

## 🧠 How It Works

1. **Describe:** Enter your software project idea.
2. **Personalize:** Select your experience level and preferred technology.
3. **Generate:** BuildVerse AI sends your request to the Flask backend.
4. **Analyze:** The backend communicates with the local Qwen model through Ollama.
5. **Plan:** The model generates a structured roadmap with features, phases, tasks, technologies, estimates, and risks.
6. **Track:** Review your plan and use the progress checklist as you develop your project.

## 🏗️ System Architecture

```text
       User Project Idea
               |
               v
    HTML, CSS and JavaScript
               |
               v
        Flask Backend
               |
               v
         Ollama API
               |
               v
          Qwen 2.5 3B
               |
               v
      Structured AI Response
               |
               v
       BuildVerse AI UI
               |
               v
  Roadmap, Tasks, Tools and Risks
```

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| HTML5 | Web page structure |
| CSS3 | Styling and layout |
| JavaScript | User interaction and API communication |
| Python | Backend programming |
| Flask | Web server and API endpoints |
| Ollama | Local AI model runtime |
| Qwen 2.5 3B | AI-powered roadmap generation |
| JSON | Structured communication between the AI backend and frontend |

## ⚙️ Getting Started

### Prerequisites

Install the following on your computer:

- Python 3.10 or a compatible Python version
- Git
- [Ollama](https://ollama.com/)
- Sufficient system resources to run the Qwen 2.5 3B model locally

### 1. Clone the Repository

```bash
git clone https://github.com/varshareddysangireddypally/BuildVerse-AI.git
cd BuildVerse-AI
```

### 2. Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install flask flask-cors requests
```

### 4. Download the AI Model

Make sure Ollama is installed and running, then execute:

```bash
ollama pull qwen2.5:3b
```

### 5. Start the Application

From the project root, run:

```bash
python app.py
```

### 6. Open BuildVerse AI

Visit the following address in your browser:

**http://127.0.0.1:5000/**

Enter your project idea and generate your roadmap!

## 📂 Project Structure

```text
BuildVerse-AI/
├── frontend/
│   └── index.html
├── app.py
├── .gitignore
└── README.md
```

The `.venv` directory is created locally during setup and is not part of the source repository.

## 🎯 Example Use Case

**Input:** AI Attendance System for Colleges

**BuildVerse AI can suggest:**
- A project summary and relevant features
- Development phases covering setup, implementation, integration, and testing
- A suitable backend and database
- Specific tasks for each phase
- Estimated development hours
- Potential risks and ways to address them

The output is an AI-generated plan that developers can review and adapt to their requirements.

## 🔐 Privacy and Limitations

- The Qwen model runs locally through Ollama, so roadmap generation does not require a paid cloud AI inference service.
- The application must be running locally, with Ollama and the required model available.
- Generated technology recommendations, task lists, and time estimates are suggestions, not guarantees.
- The current implementation uses text descriptions for project planning. Image upload or preview should not be interpreted as AI image analysis unless a vision-capable model and image-processing workflow are added.
- This project is a hackathon prototype and has not been presented as a production-ready application.

## 🚀 Future Enhancements

- 📄 Export roadmaps as PDF or project reports.
- 👥 Add user accounts and saved project roadmaps.
- 📊 Introduce richer progress analytics.
- 🧩 Improve roadmap customization and task dependency planning.
- 🖼️ Add genuine project-sketch analysis using a vision-capable model.
- ☁️ Deploy the application online for broader access.

## 💻 Project Status

**Hackathon Prototype — Core Roadmap Generation Implemented**

BuildVerse AI demonstrates how local AI can assist with software project planning. Further testing, interface refinements, and additional features can extend its capabilities.

## 👩‍💻 Developed By

**Varsha Reddy**

B.Tech — Computer Science and Engineering

Malla Reddy Engineering College for Women

## ⭐ Support the Project

If you find BuildVerse AI useful, explore the repository, try it locally, and share your feedback.

**Build smarter. Plan better. Start building with BuildVerse AI!** 🚀
