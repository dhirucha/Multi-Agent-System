# AgentMind — Multi-Agent AI Research UI

A premium, dark-theme Streamlit dashboard for your multi-agent research pipeline.

---

## Folder Structure

```
MULTI-AGENT SYSTEM/
├── app.py            ← NEW: main Streamlit app (this file)
├── styles.py         ← NEW: all CSS (imported by app.py)
├── pipeline.py       ← existing (unchanged)
├── agents.py         ← existing (unchanged)
├── tools.py          ← existing (unchanged)
├── .env              ← existing (unchanged)
├── requirements.txt  ← updated (add streamlit, plotly, pandas)
└── .venv/
```

---

## Setup

```bash
# Activate your venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows

# Install new UI deps
pip install streamlit plotly pandas

# Run the app
streamlit run app.py
```

---

## Integration

The `app.py` imports your pipeline directly:

```python
from pipeline import run_research_pipeline
```

This is already wired. Your `run_research_pipeline(topic)` must return a dict:

```python
{
    "search_results":  str,
    "scraped_content": str,
    "report":          str,
    "feedback":        str,
}
```

That matches your existing `run_research_pipeline` exactly — no changes needed.

---

## Pages

| Page | What it does |
|------|-------------|
| **Dashboard** | Hero, metrics, topic input, agent pipeline view, live logs, result tabs |
| **Research History** | All past runs with status |
| **Agents** | Detailed view of each agent's role and capabilities |
| **Settings** | LLM provider, model, temperature, search config |

---

## Demo / Dev Mode

To run without calling the real pipeline (for UI demos), swap this line in `app.py`:

```python
# Real mode (default)
from pipeline import run_research_pipeline

# Demo mode — comment above, uncomment below
# run_research_pipeline = None
```

Then remove the `result = run_research_pipeline(topic)` call and inject mock data.

---

## Customisation

- **Colors** — edit CSS variables in `styles.py` (`:root` block)
- **Fonts** — change the Google Fonts import in `styles.py`
- **Agent names** — update `agents_meta` list in `app.py`
- **Example chips** — edit `example_topics` list in `app.py`
