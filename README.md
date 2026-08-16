# AgentMind

**Multi-Agent AI Research UI** — a premium, dark-theme Streamlit dashboard for orchestrating and visualizing a multi-agent research pipeline.

---

## Overview

AgentMind wraps an existing multi-agent research pipeline (Search → Scrape → Report → Critic) in a polished Streamlit interface, giving you real-time pipeline visibility, run history, and per-agent configuration without touching the underlying pipeline code.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Pipeline Integration](#pipeline-integration)
- [Application Pages](#application-pages)
- [Demo Mode](#demo-mode)
- [Customization](#customization)
- [License](#license)

---

## Project Structure

```
agentmind/
├── app.py               # Main Streamlit application entry point
├── styles.py             # Centralized CSS/theme definitions
├── pipeline.py            # Multi-agent pipeline orchestration (unchanged)
├── agents.py              # Agent definitions and roles (unchanged)
├── tools.py               # Shared tool utilities (unchanged)
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not committed)
└── .venv/                 # Virtual environment (not committed)
```

---

## Requirements

- Python 3.9+
- An existing `pipeline.py` exposing `run_research_pipeline(topic: str) -> dict`
- API keys for your configured LLM/search providers (set via `.env`)

---

## Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/agentmind.git
cd agentmind

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
.venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
```

**New UI dependencies** (add to `requirements.txt` if not already present):

```
streamlit
plotly
pandas
```

---

## Usage

```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501` by default.

---

## Pipeline Integration

`app.py` imports the pipeline directly — no adapter or wrapper layer required:

```python
from pipeline import run_research_pipeline
```

`run_research_pipeline(topic: str)` must return a dictionary with the following shape:

```python
{
    "search_results":  str,
    "scraped_content": str,
    "report":          str,
    "feedback":        str,
}
```

This matches the existing `run_research_pipeline` implementation exactly — no changes to `pipeline.py`, `agents.py`, or `tools.py` are required.

---

## Application Pages

| Page | Description |
|---|---|
| **Dashboard** | Hero section, run metrics, topic input, live agent pipeline visualization, execution logs, and tabbed results view |
| **Research History** | Chronological log of all past runs with status and outcome |
| **Agents** | Reference view of each agent's role, responsibilities, and capabilities |
| **Settings** | Configuration for LLM provider, model selection, temperature, and search parameters |

---

## Demo Mode

To preview the UI without invoking the live pipeline (useful for demos or frontend-only development), swap the import in `app.py`:

```python
# Live mode (default)
from pipeline import run_research_pipeline

# Demo mode — comment out the import above and uncomment below
# run_research_pipeline = None
```

Then remove the `result = run_research_pipeline(topic)` call and substitute mock/sample data of the same shape described in [Pipeline Integration](#pipeline-integration).

---

## Customization

| What | Where |
|---|---|
| Color palette | CSS custom properties in the `:root` block of `styles.py` |
| Typography | Google Fonts import in `styles.py` |
| Agent metadata | `agents_meta` list in `app.py` |
| Example topic chips | `example_topics` list in `app.py` |

---

## License

Specify a license (e.g., MIT) here.
