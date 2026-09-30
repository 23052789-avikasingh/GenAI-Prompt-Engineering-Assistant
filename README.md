# Generative AI Prompt Engineering Assistant

## Project Overview
The Generative AI Prompt Engineering Assistant is a web application that converts simple user requests into structured prompts. It demonstrates practical prompt-engineering concepts such as role prompting, context specification, constraints, output formatting, and quality checks.

## Objectives
- Improve the quality and consistency of prompts.
- Demonstrate reusable prompt-engineering patterns.
- Provide a simple interactive interface.
- Generate a demo response from the optimized prompt.
- Provide a foundation for connecting an external LLM API.

## Features
- Prompt optimization
- Role selection
- Tone selection
- Audience/context specification
- Output-format selection
- Constraint handling
- Optimized prompt preview
- Demo AI response
- Responsive Streamlit interface

## Technology Stack
- Python
- Streamlit
- Prompt Engineering
- Generative AI concepts

## Project Structure
```text
GenAI_Prompt_Engineering_Assistant/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── prompts/
│   └── prompt_templates.py
├── utils/
│   └── prompt_optimizer.py
├── sample_prompts/
│   └── examples.txt
├── screenshots/
└── docs/
    ├── Project_Report.docx
    └── Project_Presentation.pptx
```

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deployment
The application can be deployed on Streamlit Community Cloud or another Python-compatible hosting platform. Set the repository root as the application source and use `app.py` as the entry point.

## API Key Safety
This version intentionally works without an API key. If an LLM provider is integrated, store the API key in the hosting platform's secrets/environment variables and never commit it to GitHub.

## Future Scope
- Connect OpenAI/Gemini/other LLM APIs.
- Add prompt history and export.
- Add prompt-quality scoring.
- Add more domain-specific templates.
- Add authentication and database storage.

## Author
Student Project — Generative AI and Prompt Engineering
