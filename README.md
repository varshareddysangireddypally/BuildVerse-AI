# BuildVerse AI 🚀
### Turn Your Project Idea Into a Realistic Development Roadmap

**Think it. Plan it. Build it.**

BuildVerse AI is an AI-powered project planning assistant that helps students and beginner developers transform software project ideas into structured, actionable development roadmaps.

Instead of wondering where to start, which technologies to choose, or how to divide a project into manageable tasks, users can describe their idea and receive an AI-generated plan to guide their development journey.

> **Core idea:** Project idea → Local AI processing → Structured development roadmap.

## 🌟 About the Project

Have a great software project idea but don't know where to start?

BuildVerse AI helps bridge the gap between having an idea and knowing how to implement it. Users enter a project description, choose their experience level and technology preference, and generate a roadmap with suggested features, development phases, tasks, tools, time estimates, and potential risks.

The application uses **Qwen 2.5 3B through Ollama** for local AI inference, with a Python Flask backend connecting the model to the web interface.

BuildVerse AI aims to make project planning simpler, more accessible, and less overwhelming for beginners.

## ✨ Key Features

- 💡 **AI-Powered Project Understanding:** Generate a concise summary of a software project idea.
- 🗺️ **Structured Roadmap Generation:** Organize development into manageable phases.
- ✅ **Task-Based Planning:** Break phases into actionable tasks and track progress using a checklist.
- 🛠️ **Technology Recommendations:** Receive suggested technologies and development tools.
- ⏱️ **Time Estimation:** View AI-generated estimates for development phases.
- ⚠️ **Risk Awareness:** Identify potential challenges and suggested mitigation strategies.
- 🎯 **Beginner-Friendly Planning:** Customize the roadmap according to the selected experience level.
- 🤖 **Local AI Inference:** Generate roadmaps using a locally running Qwen model through Ollama, without requiring a paid cloud AI inference API.
- 🌐 **Interactive Web Interface:** Enter ideas and view the generated roadmap through a browser-based application.

## 🧠 How It Works

1. **Describe:** Enter a software project idea in plain English.
2. **Personalize:** Select your experience level and preferred technology.
3. **Generate:** The frontend sends the project details to the Flask backend.
4. **Process:** The backend sends a prompt to the local Ollama API.
5. **Analyze:** Qwen 2.5 3B generates a structured development plan.
6. **Display:** BuildVerse AI presents the generated roadmap in the web interface.
7. **Track:** Review the tasks and use the progress checklist while developing the project.

### Example

**Input:** AI Attendance System for Colleges

**Possible output:**
- Project summary and suggested features
- Development phases and implementation tasks
- Recommended programming languages, frameworks, and tools
- Estimated development effort
- Potential risks and mitigation suggestions

The generated output is a starting point. Developers should review and customize it to match their actual requirements.

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
              Ollama Local API
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

### Why Is AI Important to BuildVerse AI?

The AI model is part of the core functionality, not just an optional coding assistant. It interprets a user's project description and generates a project-specific plan instead of relying exclusively on a fixed, manually written roadmap.

Ollama provides the local model runtime, while Flask handles communication between the frontend and the model.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| HTML5 | Web page structure |
| CSS3 | Interface styling and layout |
| JavaScript | User interaction and API communication |
| Python | Backend programming |
| Flask | Web server and API endpoints |
| Flask-CORS | Cross-origin request support, where needed |
| Requests | Communication with the Ollama API |
| Ollama | Local AI model runtime |
| Qwen 2.5 3B | AI-powered roadmap generation |
| JSON | Structured communication between the backend and frontend |

## ⚙️ Getting Started

BuildVerse AI is currently a **locally run prototype**. The application must be running on the computer where it is accessed.

### Prerequisites

Install the following:

- Python 3.10 or a compatible Python version
- Git
- [Ollama](https://ollama.com/)
- Sufficient memory and system resources to run Qwen 2.5 3B

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

If PowerShell blocks virtual-environment activation, you can install dependencies using the environment's Python executable directly.

### 3. Install Dependencies

If the repository contains `requirements.txt`:

```bash
pip install -r requirements.txt
```

Alternatively, install the current application dependencies directly:

```bash
pip install flask flask-cors requests
```

### 4. Download the AI Model

Install Ollama and download the model:

```bash
ollama pull qwen2.5:3b
```

Ensure Ollama is running and the model is available before generating a roadmap.

### 5. Start the Application

From the project root, run:

```bash
python app.py
```

### 6. Open BuildVerse AI

Open the following address in a browser **on the same computer running Flask**:

http://127.0.0.1:5000/

Enter a project idea, select your preferences, and generate your roadmap.

### Important: Understanding Localhost

The address `http://127.0.0.1:5000/` is a local address, not a public website link. Other people cannot open your computer's localhost by clicking that URL from their own devices.

Anyone wishing to run the project must clone the repository, install the prerequisites, download the model, and start the application locally. A publicly accessible hosted version would require additional deployment and model-inference configuration.

## 📂 Project Structure

```text
BuildVerse-AI/
├── frontend/
│   └── index.html
├── app.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

The `.venv/` directory is created locally during setup and should not be committed to the repository.

*Note: The structure above assumes `requirements.txt` and `LICENSE` are present. Include any additional files that actually exist in the repository.*

## 🎯 Example Use Case

### AI Attendance System for Colleges

A student enters:

> I want to build an AI attendance system for colleges.

BuildVerse AI can generate suggestions for:

- Student, faculty, and administrator features
- Development phases, from planning to testing
- Suitable backend, database, and AI-related tools
- Individual implementation tasks
- Estimated development hours
- Potential challenges and mitigation strategies

The roadmap helps a beginner understand the development process before writing the application.

## 🔐 Privacy, Limitations and Responsible Use

- **Local inference:** Roadmap generation uses a locally running model through Ollama. The application does not need a paid cloud AI inference API for this workflow.
- **Local execution:** Flask and Ollama must be running on the computer being used.
- **AI-generated suggestions:** Technology recommendations, task lists, and estimates may be incomplete or inaccurate. Review them before using them in a real project.
- **Image limitations:** The current text-based roadmap workflow should not be interpreted as AI image analysis. Uploading or previewing an image does not establish that the model has analyzed it.
- **Prototype status:** BuildVerse AI is a hackathon prototype and has not been represented as a production-ready application.
- **Hardware requirements:** Inference speed and reliability depend on available system resources and the local model setup.

## 🚀 Future Enhancements

- 📄 Export roadmaps as PDF or project reports.
- 👥 Add user accounts and saved project roadmaps.
- 📊 Introduce richer progress analytics.
- 🧩 Add task dependencies and more detailed roadmap customization.
- 🖼️ Integrate a vision-capable model for genuine project-sketch analysis.
- ☁️ Deploy a publicly accessible version with suitable model hosting.
- 🧪 Add automated tests, stronger output validation, and improved error handling.

## 💻 Project Status

**Hackathon Prototype — Core Roadmap Generation Implemented**

The current project demonstrates the end-to-end workflow of sending a project idea to a locally running AI model and presenting its generated development roadmap through a web interface.

Further testing, output validation, interface refinements, and additional features can improve its reliability and usability.

## 👩‍💻 Developer

**Varsha Reddy**  
B.Tech — Computer Science and Engineering  
Malla Reddy Engineering College for Women

## 📜 License

This project is released under the **MIT License**, provided that the repository includes the corresponding `LICENSE` file.

See [LICENSE](LICENSE) for the license terms.

## 🙌 Acknowledgements

- **Qwen 2.5 3B:** The model used for local AI-powered roadmap generation.
- **Ollama:** The runtime used to run the model locally.
- **Flask and the Python ecosystem:** The backend and supporting libraries.
- **AI-assisted development:** AI tools were used to support development and debugging. The repository represents the implemented project and its actual functionality.

Please refer to the relevant model and dependency licenses and terms when using or redistributing them.

---

⭐ If you find BuildVerse AI useful, explore the repository, run it locally, and share feedback.

**Build smarter. Plan better. Start building with BuildVerse AI! 🚀**
