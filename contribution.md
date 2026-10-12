# Contributing to BuildVerse AI

Thank you for your interest in contributing to BuildVerse AI!

BuildVerse AI is an AI-powered project planning assistant designed to help students and beginner developers turn ideas into actionable development roadmaps.

## How to Contribute

Contributions that improve usability, reliability, documentation, accessibility, and project-planning quality are welcome.

### 1. Fork the Repository
Fork the repository on GitHub and clone your fork to your computer.

```bash
git clone https://github.com/YOUR-USERNAME/BuildVerse-AI.git
cd BuildVerse-AI
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Set Up the Environment

Install Python and Ollama, and ensure the Qwen 2.5 3B model is available locally.

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Download the model if it is not already installed:

```bash
ollama pull qwen2.5:3b
```

### 3. Run the Application

Start Ollama and make sure the model is available. Then run:

```bash
python app.py
```

Open the local address displayed by Flask in your browser, usually `http://127.0.0.1:5000/`.

### 4. Make Your Changes

- Keep changes focused and easy to review.
- Follow the existing project structure and coding style.
- Avoid committing API keys, passwords, personal information, virtual environments, or other sensitive files.
- Update the README when setup instructions or features change.
- Test relevant functionality before submitting changes.
- Clearly identify any new dependencies.

### 5. Submit a Pull Request

1. Commit your changes with a clear message.
2. Push your branch to your fork.
3. Open a pull request against the original repository.
4. Explain what changed, why it is useful, and how you tested it.

## Areas for Improvement

Potential contribution areas include:
- More relevant and reliable AI-generated roadmaps
- Better technology recommendations for beginners
- Clearer task layouts and progress tracking
- Input validation and error handling
- Accessibility and responsive design
- Documentation and automated tests

## Reporting Issues

When reporting an issue, include:
- A clear description of the problem
- Steps to reproduce it
- Expected and actual behavior
- Relevant error messages, without secrets or private information

## Code of Conduct

Be respectful, constructive, and welcoming. Treat all contributors fairly and focus feedback on improving the project.

## License

By contributing, you agree that your contributions will be distributed under the project's MIT License, subject to applicable rights and permissions.
