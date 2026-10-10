# Does Adding a Source Make LLM Answers More Trustworthy?

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/APysnack/trustworthy-ai-project.git
cd trustworthy-ai-project
```

### 2. Create a virtual environment

macOS/Linux:
```bash
python3 -m venv .venv
```

Windows:
```bash
py -m venv .venv 
```
or
```bash
python -m venv .venv 
```

### 3. Activate the virtual environment

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Make and set Gemini API key
Go to https://ai.google.dev/gemini-api/docs/api-key to create a gemini API key.
Then, create a .env file in the project root and add
```bash
GOOGLE_API_KEY=your_api_key
```
or
```bash
GEMINI_API_KEY=your_api_key
```
to it.

### 6. Optionally set a HuggingFace token for faster database download
Go to https://huggingface.co/settings/tokens to create a read-only hugging face API token.
Then set HF_TOKEN to it in your .env file:
```bash
HF_TOKEN=your_hf_token
```

### 7. Run the project

```bash
python src/main.py
```

### 8. Deactivate the virtual environment

```bash
deactivate
```
