GLOBAL_CSS = """
<style>
/* ═══════════════════════════════════════════════════════
   FONTS
═══════════════════════════════════════════════════════ */
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap');

/* ═══════════════════════════════════════════════════════
   ROOT TOKENS
═══════════════════════════════════════════════════════ */
:root {
    --bg-base:      #070b14;
    --bg-elevated:  #0d1424;
    --bg-glass:     rgba(255,255,255,0.035);
    --bg-glass-2:   rgba(255,255,255,0.06);
    --border:       rgba(255,255,255,0.07);
    --border-glow:  rgba(99,179,237,0.35);
    --blue-1:       #63b3ed;
    --blue-2:       #3b82f6;
    --purple-1:     #a78bfa;
    --purple-2:     #7c3aed;
    --cyan:         #22d3ee;
    --green:        #4ade80;
    --red:          #f87171;
    --amber:        #fbbf24;
    --text-1:       #f0f4ff;
    --text-2:       #8b9cbf;
    --text-3:       #4a5a7a;
    --radius:       16px;
    --radius-sm:    10px;
    --radius-lg:    24px;
    --shadow:       0 8px 40px rgba(0,0,0,0.6);
    --font-display: 'Syne', sans-serif;
    --font-body:    'DM Sans', sans-serif;
    --font-mono:    'JetBrains Mono', monospace;
}

/* ═══════════════════════════════════════════════════════
   GLOBAL RESET
═══════════════════════════════════════════════════════ */
html, body, .stApp {
    background-color: var(--bg-base) !important;
    font-family: var(--font-body) !important;
    color: var(--text-1) !important;
}

/* Remove default Streamlit padding */
.block-container {
    padding: 1.5rem 2rem 4rem !important;
    max-width: 1400px !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { display: none !important; }
.stDeployButton { display: none !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: var(--bg-base); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 10px; }

/* ═══════════════════════════════════════════════════════
   SIDEBAR
═══════════════════════════════════════════════════════ */
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #0a0f1e 0%, #0d1424 100%) !important;
    border-right: 1px solid var(--border) !important;
    box-shadow: 4px 0 40px rgba(0,0,0,0.5) !important;
}
[data-testid="stSidebar"] > div {
    padding: 1.5rem 1.25rem !important;
}

.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 0.25rem;
    padding: 0.75rem;
}
.logo-icon {
    font-size: 1.8rem;
    filter: drop-shadow(0 0 8px var(--blue-1));
}
.logo-text { display: flex; flex-direction: column; }
.logo-main {
    font-family: var(--font-display);
    font-size: 1.1rem;
    font-weight: 800;
    background: linear-gradient(135deg, var(--blue-1), var(--purple-1));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 0.02em;
}
.logo-sub {
    font-size: 0.65rem;
    color: var(--text-3);
    letter-spacing: 0.12em;
    text-transform: uppercase;
}

.sidebar-divider {
    height: 1px;
    background: var(--border);
    margin: 1rem 0;
}
.sidebar-spacer { flex: 1; min-height: 1.5rem; }

/* Nav buttons */
[data-testid="stSidebar"] .stButton > button {
    background: transparent !important;
    border: 1px solid transparent !important;
    color: var(--text-2) !important;
    font-family: var(--font-body) !important;
    font-size: 0.875rem !important;
    text-align: left !important;
    border-radius: var(--radius-sm) !important;
    padding: 0.6rem 1rem !important;
    transition: all 0.2s !important;
    width: 100% !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background: var(--bg-glass-2) !important;
    border-color: var(--border-glow) !important;
    color: var(--text-1) !important;
    transform: translateX(2px) !important;
}

.sidebar-section-title {
    font-size: 0.6rem;
    color: var(--text-3);
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin: 0.75rem 0 0.5rem !important;
    padding: 0 0.25rem;
}

.sidebar-agent-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.4rem 0.5rem;
    border-radius: var(--radius-sm);
    margin-bottom: 0.25rem;
    font-size: 0.78rem;
    color: var(--text-2);
    background: var(--bg-glass);
    border: 1px solid var(--border);
}

.user-profile-card {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem;
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    margin-top: 0.5rem;
    position: relative;
}
.user-avatar {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, var(--blue-2), var(--purple-2));
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-weight: 700; font-size: 0.9rem; color: white;
    flex-shrink: 0;
}
.user-name { font-size: 0.85rem; font-weight: 600; color: var(--text-1); }
.user-role { font-size: 0.7rem; color: var(--text-3); }
.user-status-dot {
    width: 8px; height: 8px;
    background: var(--green);
    border-radius: 50%;
    position: absolute; top: 12px; right: 12px;
    box-shadow: 0 0 6px var(--green);
    animation: pulse 2s infinite;
}

/* ═══════════════════════════════════════════════════════
   HERO SECTION
═══════════════════════════════════════════════════════ */
.hero-section {
    position: relative;
    background: linear-gradient(135deg, #070b14 0%, #0d1424 40%, #0a1229 100%);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 4rem 3rem;
    margin-bottom: 2rem;
    overflow: hidden;
    text-align: center;
}
.hero-glow {
    position: absolute;
    top: -60px; left: 50%;
    transform: translateX(-50%);
    width: 600px; height: 300px;
    background: radial-gradient(ellipse, rgba(99,179,237,0.12) 0%, transparent 70%);
    pointer-events: none;
}
.hero-badge {
    display: inline-block;
    background: rgba(99,179,237,0.1);
    border: 1px solid rgba(99,179,237,0.3);
    border-radius: 100px;
    padding: 0.3rem 1rem;
    font-size: 0.75rem;
    color: var(--blue-1);
    letter-spacing: 0.08em;
    margin-bottom: 1.25rem;
    font-family: var(--font-mono);
}
.hero-title {
    font-family: var(--font-display) !important;
    font-size: clamp(2rem, 4vw, 3.2rem) !important;
    font-weight: 800 !important;
    color: var(--text-1) !important;
    margin: 0 0 1rem !important;
    line-height: 1.1 !important;
    letter-spacing: -0.02em;
}
.gradient-text {
    background: linear-gradient(135deg, var(--blue-1) 0%, var(--purple-1) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-subtitle {
    font-size: 1rem;
    color: var(--text-2);
    line-height: 1.7;
    max-width: 580px;
    margin: 0 auto;
}

/* ═══════════════════════════════════════════════════════
   SECTION TITLES
═══════════════════════════════════════════════════════ */
.section-title {
    font-family: var(--font-display);
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--text-2);
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 1rem;
}
.page-title {
    font-family: var(--font-display) !important;
    font-size: 1.8rem !important;
    font-weight: 800 !important;
    color: var(--text-1) !important;
    margin-bottom: 1.5rem !important;
}

/* ═══════════════════════════════════════════════════════
   METRIC CARDS
═══════════════════════════════════════════════════════ */
.metric-card {
    display: flex;
    align-items: center;
    gap: 1rem;
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.25rem 1.5rem;
    transition: all 0.3s;
}
.metric-card:hover {
    border-color: var(--border-glow);
    background: var(--bg-glass-2);
    transform: translateY(-2px);
    box-shadow: 0 8px 32px rgba(99,179,237,0.08);
}
.metric-icon { font-size: 1.8rem; }
.metric-label {
    font-size: 0.7rem;
    color: var(--text-3);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.2rem;
}
.metric-value {
    font-family: var(--font-display);
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-1);
    line-height: 1.1;
}
.metric-sub { font-size: 0.7rem; color: var(--text-3); margin-top: 0.2rem; }

/* ═══════════════════════════════════════════════════════
   INPUT OVERRIDES
═══════════════════════════════════════════════════════ */
.stTextInput > div > div > input {
    background: var(--bg-glass) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    color: var(--text-1) !important;
    font-family: var(--font-body) !important;
    font-size: 1rem !important;
    padding: 0.9rem 1.25rem !important;
    transition: all 0.3s !important;
}
.stTextInput > div > div > input:focus {
    border-color: var(--blue-1) !important;
    box-shadow: 0 0 0 3px rgba(99,179,237,0.15) !important;
    outline: none !important;
}
.stTextInput > div > div > input::placeholder { color: var(--text-3) !important; }

/* Primary buttons */
.stButton > button[kind="primary"],
.stButton > button[data-testid*="primary"] {
    background: linear-gradient(135deg, var(--blue-2), var(--purple-2)) !important;
    border: none !important;
    color: white !important;
    font-family: var(--font-display) !important;
    font-weight: 700 !important;
    border-radius: var(--radius) !important;
    padding: 0.7rem 1.25rem !important;
    transition: all 0.25s !important;
    box-shadow: 0 4px 20px rgba(59,130,246,0.35) !important;
}
.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(59,130,246,0.5) !important;
}

/* Chip buttons */
.chips-row .stButton > button {
    background: var(--bg-glass) !important;
    border: 1px solid var(--border) !important;
    color: var(--text-2) !important;
    font-size: 0.75rem !important;
    border-radius: 100px !important;
    padding: 0.35rem 0.8rem !important;
    font-family: var(--font-mono) !important;
    transition: all 0.2s !important;
}
.chips-row .stButton > button:hover {
    border-color: var(--blue-1) !important;
    color: var(--blue-1) !important;
    background: rgba(99,179,237,0.08) !important;
}

/* ═══════════════════════════════════════════════════════
   AGENT CARDS
═══════════════════════════════════════════════════════ */
.agent-card {
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.5rem 1.25rem;
    text-align: center;
    transition: all 0.3s;
    position: relative;
    min-height: 180px;
}
.agent-card:hover {
    border-color: var(--border-glow);
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(99,179,237,0.1);
}
.card-glow {
    border-color: rgba(99,179,237,0.6) !important;
    box-shadow: 0 0 30px rgba(99,179,237,0.25) !important;
    animation: cardPulse 1.5s ease-in-out infinite;
}
@keyframes cardPulse {
    0%, 100% { box-shadow: 0 0 20px rgba(99,179,237,0.2); }
    50%       { box-shadow: 0 0 40px rgba(99,179,237,0.45); }
}
.agent-icon { font-size: 2rem; margin-bottom: 0.5rem; }
.agent-name {
    font-family: var(--font-display);
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--text-1);
    margin-bottom: 0.5rem;
}
.agent-desc { font-size: 0.75rem; color: var(--text-2); line-height: 1.5; margin-bottom: 1rem; }

/* ═══════════════════════════════════════════════════════
   PIPELINE CONNECTOR
═══════════════════════════════════════════════════════ */
.pipeline-connector {
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0.75rem 0;
    gap: 0.5rem;
}
.pipeline-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border-glow), transparent);
    max-width: 900px;
}

/* ═══════════════════════════════════════════════════════
   STATUS BADGES
═══════════════════════════════════════════════════════ */
.status-badge {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 0.62rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    padding: 0.2rem 0.6rem;
    border-radius: 100px;
    border: 1px solid transparent;
}
.badge-idle      { background: rgba(75,85,99,0.25);   border-color: rgba(75,85,99,0.5);    color: #9ca3af; }
.badge-running   { background: rgba(59,130,246,0.15);  border-color: rgba(59,130,246,0.5);  color: var(--blue-1); animation: badgePulse 1s infinite; }
.badge-completed { background: rgba(74,222,128,0.12);  border-color: rgba(74,222,128,0.4);  color: var(--green); }
.badge-failed    { background: rgba(248,113,113,0.12); border-color: rgba(248,113,113,0.4); color: var(--red); }
@keyframes badgePulse {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0.5; }
}

/* ═══════════════════════════════════════════════════════
   TERMINAL
═══════════════════════════════════════════════════════ */
.terminal-window {
    background: #050810;
    border: 1px solid rgba(74,222,128,0.2);
    border-radius: var(--radius);
    overflow: hidden;
    font-family: var(--font-mono);
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 40px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.04);
}
.terminal-header {
    background: rgba(255,255,255,0.04);
    border-bottom: 1px solid rgba(255,255,255,0.05);
    padding: 0.6rem 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.t-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    display: inline-block;
}
.t-dot.red    { background: #ff5f57; }
.t-dot.yellow { background: #ffbd2e; }
.t-dot.green  { background: #28c940; }
.terminal-title {
    font-size: 0.7rem;
    color: var(--text-3);
    margin-left: 0.5rem;
    letter-spacing: 0.1em;
}
.terminal-body {
    padding: 1.25rem 1.5rem;
    max-height: 340px;
    overflow-y: auto;
    background: repeating-linear-gradient(
        0deg,
        rgba(255,255,255,0.005) 0px,
        rgba(255,255,255,0.005) 1px,
        transparent 1px,
        transparent 22px
    );
}
.log-line {
    display: flex;
    gap: 0.75rem;
    font-size: 0.8rem;
    line-height: 1.8;
    white-space: pre-wrap;
}
.log-ts    { color: var(--text-3); flex-shrink: 0; }
.log-info  .log-msg { color: #86efac; }
.log-step  .log-msg { color: var(--blue-1); font-weight: 600; }
.log-success .log-msg { color: var(--green); font-weight: 600; }
.log-error .log-msg { color: var(--red); }
.cursor-blink {
    color: var(--green);
    font-size: 0.85rem;
    animation: blink 1s step-end infinite;
    display: inline-block;
    margin-top: 0.25rem;
}
@keyframes blink {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0; }
}

/* ═══════════════════════════════════════════════════════
   TABS
═══════════════════════════════════════════════════════ */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 1px solid var(--border) !important;
    gap: 0.25rem;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    border: none !important;
    color: var(--text-2) !important;
    font-family: var(--font-body) !important;
    font-size: 0.85rem !important;
    padding: 0.6rem 1rem !important;
    border-radius: var(--radius-sm) var(--radius-sm) 0 0 !important;
    transition: all 0.2s !important;
}
.stTabs [aria-selected="true"] {
    background: var(--bg-glass-2) !important;
    color: var(--blue-1) !important;
    border-bottom: 2px solid var(--blue-1) !important;
}
.stTabs [data-baseweb="tab-panel"] {
    padding: 1.25rem 0 !important;
}

/* ═══════════════════════════════════════════════════════
   RESULT CARDS
═══════════════════════════════════════════════════════ */
.result-card {
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.75rem;
    font-size: 0.9rem;
    line-height: 1.8;
    color: var(--text-1);
    max-height: 520px;
    overflow-y: auto;
}
.report-card {
    background: #080c18;
}
.result-card h1, .result-card h2, .result-card h3 {
    font-family: var(--font-display) !important;
    color: var(--text-1) !important;
}
.result-card code {
    background: rgba(255,255,255,0.06) !important;
    border-radius: 4px !important;
    padding: 0.1rem 0.4rem !important;
    font-family: var(--font-mono) !important;
    color: var(--cyan) !important;
}

/* ═══════════════════════════════════════════════════════
   DOWNLOAD BUTTONS
═══════════════════════════════════════════════════════ */
.stDownloadButton > button {
    background: var(--bg-glass) !important;
    border: 1px solid var(--border) !important;
    color: var(--text-1) !important;
    border-radius: var(--radius) !important;
    font-family: var(--font-body) !important;
    transition: all 0.2s !important;
    padding: 0.6rem 1.25rem !important;
}
.stDownloadButton > button:hover {
    border-color: var(--blue-1) !important;
    color: var(--blue-1) !important;
}

/* ═══════════════════════════════════════════════════════
   HISTORY
═══════════════════════════════════════════════════════ */
.history-row {
    display: flex;
    align-items: center;
    gap: 1.25rem;
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1rem 1.5rem;
    margin-bottom: 0.6rem;
    transition: all 0.2s;
}
.history-row:hover { border-color: var(--border-glow); transform: translateX(3px); }
.history-index { font-family: var(--font-mono); color: var(--text-3); font-size: 0.8rem; min-width: 2rem; }
.history-topic { flex: 1; font-weight: 500; color: var(--text-1); }
.history-time { font-size: 0.75rem; color: var(--text-3); font-family: var(--font-mono); }

/* ═══════════════════════════════════════════════════════
   AGENT DETAIL CARDS (Agents page)
═══════════════════════════════════════════════════════ */
.agent-detail-card {
    display: flex;
    gap: 1.5rem;
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.75rem;
    margin-bottom: 1rem;
    transition: all 0.3s;
}
.agent-detail-card:hover {
    border-color: var(--border-glow);
    box-shadow: 0 8px 32px rgba(99,179,237,0.07);
}
.agent-detail-icon { font-size: 2.5rem; }
.agent-detail-body { flex: 1; }
.agent-detail-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.75rem; }
.agent-detail-name { font-family: var(--font-display); font-size: 1.1rem; font-weight: 700; color: var(--text-1); }
.agent-detail-role { font-size: 0.75rem; color: var(--blue-1); font-family: var(--font-mono); }
.agent-detail-desc { font-size: 0.875rem; color: var(--text-2); line-height: 1.7; margin-bottom: 1rem; }
.skills-row { display: flex; gap: 0.5rem; flex-wrap: wrap; }
.skill-chip {
    background: rgba(99,179,237,0.08);
    border: 1px solid rgba(99,179,237,0.2);
    border-radius: 100px;
    padding: 0.2rem 0.7rem;
    font-size: 0.7rem;
    color: var(--blue-1);
    font-family: var(--font-mono);
}

/* ═══════════════════════════════════════════════════════
   SETTINGS
═══════════════════════════════════════════════════════ */
.settings-section {
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.75rem;
    margin-bottom: 1.25rem;
}
.settings-title {
    font-family: var(--font-display);
    font-weight: 700;
    font-size: 1rem;
    color: var(--text-1);
    margin-bottom: 1.25rem;
}

/* Selectbox, number input, slider */
.stSelectbox > div > div, .stNumberInput > div > div > input {
    background: var(--bg-glass) !important;
    border-color: var(--border) !important;
    color: var(--text-1) !important;
    border-radius: var(--radius-sm) !important;
}
.stSlider > div > div > div {
    background: linear-gradient(90deg, var(--blue-2), var(--purple-2)) !important;
}

/* ═══════════════════════════════════════════════════════
   EMPTY STATE
═══════════════════════════════════════════════════════ */
.empty-state {
    text-align: center;
    padding: 4rem 2rem;
    border: 1px dashed var(--border);
    border-radius: var(--radius-lg);
    margin: 2rem 0;
}
.empty-icon { font-size: 3rem; margin-bottom: 1rem; }
.empty-text { font-family: var(--font-display); font-size: 1.1rem; font-weight: 700; color: var(--text-1); }
.empty-sub { font-size: 0.85rem; color: var(--text-2); margin-top: 0.4rem; }

/* ═══════════════════════════════════════════════════════
   SUCCESS / WARNING / INFO boxes
═══════════════════════════════════════════════════════ */
.stSuccess, .stWarning, .stInfo, .stError {
    border-radius: var(--radius) !important;
}

/* ═══════════════════════════════════════════════════════
   ANIMATIONS
═══════════════════════════════════════════════════════ */
@keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 1; }
    50%       { transform: scale(1.2); opacity: 0.7; }
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}
.hero-section  { animation: fadeUp 0.6s ease both; }
.metric-card   { animation: fadeUp 0.6s ease both; }
.agent-card    { animation: fadeUp 0.5s ease both; }
</style>
"""