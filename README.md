# AI Prompt Optimizer

A Streamlit application that helps optimize prompts for various Large Language Models (LLMs) like ChatGPT, Gemini, and Claude.

## Features

- Optimize prompts for different styles (General, Technical, Creative, Academic, Business)
- Real-time prompt enhancement using OpenAI's GPT-4
- Interactive web interface built with Streamlit
- Clear explanation of optimizations made to the prompt

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd prompt-optimizer
```

2. Create a virtual environment and activate it:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run main.py
```

2. Open your web browser and go to `http://localhost:8501`

3. Enter your prompt in the text area and select the desired optimization style

4. Click "Optimize Prompt" to get the enhanced version

## Requirements

- Python 3.8+
- OpenAI API key
- Required packages listed in `requirements.txt`

## License

This project is licensed under the MIT License - see the LICENSE file for details. 