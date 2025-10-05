# Fact-Check Agent

This project is an AI-powered agent that can perform unbiased searches using **DuckDuckGo**, cross-check information with **Wikipedia**, and generate fact-check reports saved to a file.

It leverages **LangChain** to orchestrate the agent workflow and can run with different Large Language Models (LLMs). In this project, I used **Google Gemini**, but you can swap in other LLMs (e.g., OpenAI, Anthropic, etc.) with minimal changes.

---

## Features

* 🔎 Perform unbiased web searches via DuckDuckGo
* 📚 Verify information against Wikipedia
* 📝 Automatically generate and save reports as text files
* 🤖 Works with multiple LLMs (default: Gemini)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
cd REPO_NAME
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` yet, the main dependencies are:

```bash
pip install langchain duckduckgo-search wikipedia-api
```

(Plus the LLM provider SDK — e.g., `google-generativeai` for Gemini.)

---

## Usage

1. Set your API key for the LLM you want to use (example with Gemini):

```bash
export GOOGLE_API_KEY="your_api_key_here"
```

2. Run the agent:

```bash
python main.py
```

3. The agent will:

   * Search DuckDuckGo
   * Cross-check with Wikipedia
   * Create a fact-check report
   * Save it into a file (e.g., `report.txt`)

---

## Customization

* Swap in another LLM (e.g., OpenAI’s GPT) by adjusting the LangChain LLM setup.
* Change the output format to JSON, Markdown, or other file types.
* Extend the agent with additional fact-checking sources.

---

## License

MIT License. Free to use and modify.
