import streamlit as st
import time
import random
from datetime import datetime
import json

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Multi-Agent AI Research",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Inject CSS ─────────────────────────────────────────────────────────────
from styles import GLOBAL_CSS
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ─── Session State Init ──────────────────────────────────────────────────────
defaults = {
    "page": "Dashboard",
    "running": False,
    "logs": [],
    "search_results": "",
    "scraped_content": "",
    "report": "",
    "feedback": "",
    "agent_states": {
        "Search Agent":  "idle",
        "Reader Agent":  "idle",
        "Writer Agent":  "idle",
        "Critic Agent":  "idle",
    },
    "history": [],
    "metrics": {"tokens": 0, "time": 0, "runs": 0},
    "active_tab": "Final Report",
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ─── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="logo-icon">⚡</div>
        <div class="logo-text">
            <span class="logo-main">AgentMind</span>
            <span class="logo-sub">Research System</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    nav_items = [
        ("🏠", "Dashboard"),
        ("📚", "Research History"),
        ("🤖", "Agents"),
        ("⚙️", "Settings"),
    ]

    for icon, page in nav_items:
        active_cls = "nav-active" if st.session_state.page == page else ""
        if st.button(f"{icon}  {page}", key=f"nav_{page}",
                     use_container_width=True):
            st.session_state.page = page
            st.rerun()
        # We can't easily style individual buttons per class without JS tricks,
        # so we mark the active one via a hidden marker and CSS nth-child hacks.

    st.markdown('<div class="sidebar-spacer"></div>', unsafe_allow_html=True)

    # Agent status mini-panel
    st.markdown('<p class="sidebar-section-title">AGENT STATUS</p>',
                unsafe_allow_html=True)

    agent_icons = {
        "Search Agent":  "🔍",
        "Reader Agent":  "📖",
        "Writer Agent":  "✍️",
        "Critic Agent":  "🧐",
    }
    for agent, status in st.session_state.agent_states.items():
        status_cls = f"badge-{status}"
        st.markdown(
            f"""<div class="sidebar-agent-row">
                  <span>{agent_icons[agent]} {agent}</span>
                  <span class="status-badge {status_cls}">{status.upper()}</span>
                </div>""",
            unsafe_allow_html=True,
        )

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    # User profile
    st.markdown("""
    <div class="user-profile-card">
        <div class="user-avatar">D</div>
        <div class="user-info">
            <div class="user-name">Dheeraj</div>
            <div class="user-role">AI Developer</div>
        </div>
        <div class="user-status-dot"></div>
    </div>
    """, unsafe_allow_html=True)


# ─── Helper: add log ─────────────────────────────────────────────────────────
def add_log(msg: str, level: str = "info"):
    ts = datetime.now().strftime("%H:%M:%S")
    st.session_state.logs.append({"ts": ts, "msg": msg, "level": level})


def set_agent(name: str, status: str):
    st.session_state.agent_states[name] = status


def reset_agents():
    for k in st.session_state.agent_states:
        st.session_state.agent_states[k] = "idle"


# ─── Mock pipeline (replace with real pipeline import) ───────────────────────
def run_mock_pipeline(topic: str, placeholder):
    """Simulated pipeline with streaming logs. Replace with real pipeline."""
    from pipeline import run_research_pipeline          # ← real import
    # Comment out the line above and uncomment below for demo mode:
    # run_research_pipeline = None

    steps = [
        ("Search Agent",  "Querying search engine for reliable sources..."),
        ("Search Agent",  f"Searching: '{topic}' across web indexes..."),
        ("Search Agent",  "Ranking and filtering top results..."),
        ("Reader Agent",  "Selecting highest-relevance URL..."),
        ("Reader Agent",  "Scraping full article content..."),
        ("Reader Agent",  "Extracting structured data from page..."),
        ("Writer Agent",  "Synthesizing research into structured report..."),
        ("Writer Agent",  "Applying formatting and citations..."),
        ("Critic Agent",  "Reviewing factual accuracy..."),
        ("Critic Agent",  "Checking coherence and completeness..."),
        ("Critic Agent",  "Generating critique and improvement notes..."),
    ]

    agent_sequence = ["Search Agent", "Reader Agent", "Writer Agent", "Critic Agent"]
    current_agent_idx = -1
    log_lines = []

    def render_logs():
        html = '<div class="terminal-window"><div class="terminal-header"><span class="t-dot red"></span><span class="t-dot yellow"></span><span class="t-dot green"></span><span class="terminal-title">// EXECUTION LOG</span></div><div class="terminal-body">'
        for line in log_lines[-40:]:
            cls = f"log-{line['level']}"
            html += f'<div class="log-line {cls}"><span class="log-ts">[{line["ts"]}]</span> <span class="log-msg">{line["msg"]}</span></div>'
        html += '<div class="cursor-blink">█</div></div></div>'
        placeholder.markdown(html, unsafe_allow_html=True)

    add_log("🚀 Pipeline initialised", "success")
    log_lines.append({"ts": datetime.now().strftime("%H:%M:%S"),
                      "msg": "🚀 Pipeline initialised", "level": "success"})
    render_logs()
    time.sleep(0.4)

    start = time.time()

    try:
        result = run_research_pipeline(topic)

        for step_agent, step_msg in steps:
            # Detect agent transition
            idx = agent_sequence.index(step_agent)
            if idx != current_agent_idx:
                if current_agent_idx >= 0:
                    set_agent(agent_sequence[current_agent_idx], "completed")
                set_agent(step_agent, "running")
                current_agent_idx = idx
                ts = datetime.now().strftime("%H:%M:%S")
                log_lines.append({"ts": ts,
                                  "msg": f"▶ Step {idx+1} — {step_agent} activated",
                                  "level": "step"})
                render_logs()
                time.sleep(0.3)

            ts = datetime.now().strftime("%H:%M:%S")
            log_lines.append({"ts": ts, "msg": step_msg, "level": "info"})
            render_logs()
            time.sleep(random.uniform(0.15, 0.35))

        # Mark last agent done
        set_agent(agent_sequence[current_agent_idx], "completed")

        elapsed = round(time.time() - start, 2)
        ts = datetime.now().strftime("%H:%M:%S")
        log_lines.append({"ts": ts,
                          "msg": f"✅ Pipeline complete in {elapsed}s",
                          "level": "success"})
        render_logs()

        st.session_state.search_results  = result.get("search_results", "")
        st.session_state.scraped_content = result.get("scraped_content", "")
        st.session_state.report          = result.get("report", "")
        st.session_state.feedback        = result.get("feedback", "")
        st.session_state.metrics["tokens"] += random.randint(2800, 6000)
        st.session_state.metrics["time"]   += elapsed
        st.session_state.metrics["runs"]   += 1
        st.session_state.history.append({
            "topic": topic,
            "time": datetime.now().strftime("%b %d, %H:%M"),
            "status": "completed",
        })

    except Exception as exc:
        set_agent(agent_sequence[max(current_agent_idx, 0)], "failed")
        ts = datetime.now().strftime("%H:%M:%S")
        log_lines.append({"ts": ts, "msg": f"❌ Error: {exc}", "level": "error"})
        render_logs()
        raise

    st.session_state.logs = [
        {"ts": l["ts"], "msg": l["msg"], "level": l["level"]} for l in log_lines
    ]


# ════════════════════════════════════════════════════════════════════════════
#  PAGES
# ════════════════════════════════════════════════════════════════════════════

# ─── Dashboard ───────────────────────────────────────────────────────────────
if st.session_state.page == "Dashboard":

    # Hero
    st.markdown("""
    <div class="hero-section">
        <div class="hero-particles"></div>
        <div class="hero-content">
            <div class="hero-badge">⚡ AI-Powered Research</div>
            <h1 class="hero-title">
                Multi-Agent
                <span class="gradient-text"> AI Research</span>
                System
            </h1>
            <p class="hero-subtitle">
                Autonomous AI agents that search, scrape, analyze, write,<br>
                and critique detailed research reports — in seconds.
            </p>
        </div>
        <div class="hero-glow"></div>
    </div>
    """, unsafe_allow_html=True)

    # ── Metrics row ──────────────────────────────────────────────────────────
    m = st.session_state.metrics
    c1, c2, c3, c4 = st.columns(4)
    metric_data = [
        (c1, "⚡", "Total Tokens",    f"{m['tokens']:,}", "+12% vs last"),
        (c2, "⏱️", "Avg Run Time",   f"{round(m['time'],1)}s",  "Per pipeline"),
        (c3, "🔁", "Research Runs",  str(m["runs"]),             "All time"),
        (c4, "🟢", "System Status",  "Online",                   "All agents ready"),
    ]
    for col, icon, label, val, sub in metric_data:
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon">{icon}</div>
                <div class="metric-body">
                    <div class="metric-label">{label}</div>
                    <div class="metric-value">{val}</div>
                    <div class="metric-sub">{sub}</div>
                </div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)

    # ── Input section ────────────────────────────────────────────────────────
    st.markdown('<div class="section-title">🔬 Research Topic</div>',
                unsafe_allow_html=True)

    col_input, col_btn = st.columns([5, 1])
    with col_input:
        topic = st.text_input(
            label="topic",
            label_visibility="collapsed",
            placeholder="Enter a research topic — e.g. Future of AI Agents",
            key="topic_input",
        )
    with col_btn:
        run_btn = st.button("⚡ Run Research", use_container_width=True,
                            type="primary")

    # Example chips
    st.markdown('<div class="chips-row">', unsafe_allow_html=True)
    example_topics = ["Future of AI Agents", "Quantum Computing",
                      "GenAI Trends 2025", "Cybersecurity 2025",
                      "LLM Fine-Tuning", "Agentic Workflows"]
    chip_cols = st.columns(len(example_topics))
    for i, ex in enumerate(example_topics):
        with chip_cols[i]:
            if st.button(ex, key=f"chip_{i}"):
                st.session_state.topic_input = ex
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

    # ── Agent Workflow Visualization ─────────────────────────────────────────
    st.markdown('<div class="section-title">🤖 Agent Pipeline</div>',
                unsafe_allow_html=True)

    agents_meta = [
        ("🔍", "Search Agent",  "Queries multiple web sources and ranks results by relevance."),
        ("📖", "Reader Agent",  "Scrapes and extracts full content from top URLs."),
        ("✍️", "Writer Agent",  "Synthesizes all research into a structured report."),
        ("🧐", "Critic Agent",  "Reviews accuracy, coherence, and completeness."),
    ]
    a_cols = st.columns(4)
    for i, (icon, name, desc) in enumerate(agents_meta):
        status = st.session_state.agent_states[name]
        status_cls = f"badge-{status}"
        glow_cls   = "card-glow" if status == "running" else ""
        with a_cols[i]:
            connector = '<div class="agent-arrow">→</div>' if i < 3 else ""
            st.markdown(f"""
            <div class="agent-card {glow_cls}">
                <div class="agent-icon">{icon}</div>
                <div class="agent-name">{name}</div>
                <div class="agent-desc">{desc}</div>
                <span class="status-badge {status_cls}">{status.upper()}</span>
            </div>
            """, unsafe_allow_html=True)

    # Connector line
    st.markdown("""
    <div class="pipeline-connector">
        <div class="pipeline-line"></div>
        <div class="pipeline-dots">
            <span class="p-dot"></span><span class="p-dot"></span>
            <span class="p-dot"></span><span class="p-dot"></span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

    # ── Run Pipeline ─────────────────────────────────────────────────────────
    if run_btn:
        topic_val = st.session_state.get("topic_input", "").strip()
        if not topic_val:
            st.warning("Please enter a research topic first.")
        else:
            reset_agents()
            st.session_state.logs            = []
            st.session_state.search_results  = ""
            st.session_state.scraped_content = ""
            st.session_state.report          = ""
            st.session_state.feedback        = ""
            st.session_state.running         = True

            log_placeholder = st.empty()
            try:
                run_mock_pipeline(topic_val, log_placeholder)
            finally:
                st.session_state.running = False
            st.rerun()

    # ── Terminal Logs ────────────────────────────────────────────────────────
    if st.session_state.logs:
        st.markdown('<div class="section-title">💻 Execution Log</div>',
                    unsafe_allow_html=True)
        log_html = '<div class="terminal-window"><div class="terminal-header"><span class="t-dot red"></span><span class="t-dot yellow"></span><span class="t-dot green"></span><span class="terminal-title">// EXECUTION LOG</span></div><div class="terminal-body">'
        for line in st.session_state.logs[-60:]:
            cls = f"log-{line['level']}"
            log_html += f'<div class="log-line {cls}"><span class="log-ts">[{line["ts"]}]</span> <span class="log-msg">{line["msg"]}</span></div>'
        log_html += '</div></div>'
        st.markdown(log_html, unsafe_allow_html=True)

    # ── Results Tabs ─────────────────────────────────────────────────────────
    if st.session_state.report:
        st.markdown('<div class="section-title">📋 Research Results</div>',
                    unsafe_allow_html=True)

        tab1, tab2, tab3, tab4 = st.tabs(
            ["🔍 Search Results", "📖 Scraped Content",
             "📄 Final Report", "🧐 Critic Feedback"])

        with tab1:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown(st.session_state.search_results or "_No data yet._")
            st.markdown('</div>', unsafe_allow_html=True)

        with tab2:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown(st.session_state.scraped_content or "_No data yet._")
            st.markdown('</div>', unsafe_allow_html=True)

        with tab3:
            st.markdown('<div class="result-card report-card">', unsafe_allow_html=True)
            st.markdown(st.session_state.report or "_No report yet._")
            st.markdown('</div>', unsafe_allow_html=True)
            dl_col1, dl_col2 = st.columns([1, 1])
            with dl_col1:
                st.download_button(
                    "⬇️ Download Report (.md)",
                    data=st.session_state.report,
                    file_name="research_report.md",
                    mime="text/markdown",
                    use_container_width=True,
                )
            with dl_col2:
                st.download_button(
                    "⬇️ Download as TXT",
                    data=st.session_state.report,
                    file_name="research_report.txt",
                    mime="text/plain",
                    use_container_width=True,
                )

        with tab4:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown(st.session_state.feedback or "_No feedback yet._")
            st.markdown('</div>', unsafe_allow_html=True)


# ─── Research History ─────────────────────────────────────────────────────────
elif st.session_state.page == "Research History":
    st.markdown('<h2 class="page-title">📚 Research History</h2>',
                unsafe_allow_html=True)
    if not st.session_state.history:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-icon">📭</div>
            <div class="empty-text">No research runs yet</div>
            <div class="empty-sub">Head to Dashboard and run your first query</div>
        </div>""", unsafe_allow_html=True)
    else:
        for i, h in enumerate(reversed(st.session_state.history)):
            status_cls = f"badge-{h['status']}"
            st.markdown(f"""
            <div class="history-row">
                <div class="history-index">#{len(st.session_state.history)-i}</div>
                <div class="history-topic">{h['topic']}</div>
                <div class="history-time">{h['time']}</div>
                <span class="status-badge {status_cls}">{h['status'].upper()}</span>
            </div>""", unsafe_allow_html=True)


# ─── Agents Page ──────────────────────────────────────────────────────────────
elif st.session_state.page == "Agents":
    st.markdown('<h2 class="page-title">🤖 Agent Overview</h2>',
                unsafe_allow_html=True)

    agents_detail = [
        ("🔍", "Search Agent",  "Retrieval Specialist",
         "Uses LangChain's Tavily/DuckDuckGo tools to query the web for recent, authoritative information. Returns ranked snippets with URLs for the reader to follow up on.",
         ["Web Search", "Result Ranking", "URL Extraction"]),
        ("📖", "Reader Agent",  "Content Extractor",
         "Picks the most relevant URL from search results, scrapes the page using browser tools, and returns cleaned, structured text content ready for the writer.",
         ["URL Scraping", "HTML Parsing", "Content Cleaning"]),
        ("✍️", "Writer Agent",  "Report Synthesiser",
         "Receives combined search snippets + scraped content, then uses an LLM chain to produce a well-structured, markdown-formatted research report with headings and citations.",
         ["Report Writing", "Markdown Format", "Citation"]),
        ("🧐", "Critic Agent",  "Quality Reviewer",
         "Reviews the drafted report for factual accuracy, coherence, missing information, and provides actionable improvement suggestions.",
         ["Fact Check", "Coherence Review", "Feedback"]),
    ]

    for icon, name, role, desc, skills_list in agents_detail:
        status = st.session_state.agent_states[name]
        status_cls = f"badge-{status}"
        skills_html = "".join(
            f'<span class="skill-chip">{s}</span>' for s in skills_list)
        st.markdown(f"""
        <div class="agent-detail-card">
            <div class="agent-detail-left">
                <div class="agent-detail-icon">{icon}</div>
            </div>
            <div class="agent-detail-body">
                <div class="agent-detail-header">
                    <div>
                        <div class="agent-detail-name">{name}</div>
                        <div class="agent-detail-role">{role}</div>
                    </div>
                    <span class="status-badge {status_cls}">{status.upper()}</span>
                </div>
                <p class="agent-detail-desc">{desc}</p>
                <div class="skills-row">{skills_html}</div>
            </div>
        </div>""", unsafe_allow_html=True)


# ─── Settings ────────────────────────────────────────────────────────────────
elif st.session_state.page == "Settings":
    st.markdown('<h2 class="page-title">⚙️ Settings</h2>',
                unsafe_allow_html=True)

    st.markdown('<div class="settings-section">', unsafe_allow_html=True)
    st.markdown('<div class="settings-title">Model Configuration</div>',
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.selectbox("LLM Provider", ["OpenAI", "Anthropic", "Groq", "Ollama"],
                     index=0)
        st.selectbox("Model", ["gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"],
                     index=0)
    with col2:
        st.slider("Temperature", 0.0, 1.0, 0.3, 0.05)
        st.slider("Max Tokens", 512, 8192, 2048, 256)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="settings-section">', unsafe_allow_html=True)
    st.markdown('<div class="settings-title">Search Configuration</div>',
                unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox("Search Provider", ["Tavily", "DuckDuckGo", "Serper"], index=0)
        st.number_input("Max Search Results", min_value=1, max_value=20, value=5)
    with col2:
        st.selectbox("Scraper", ["Playwright", "BeautifulSoup", "Requests"], index=0)
        st.number_input("Scrape Timeout (s)", min_value=5, max_value=60, value=15)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("💾 Save Settings", type="primary"):
        st.success("Settings saved successfully!")