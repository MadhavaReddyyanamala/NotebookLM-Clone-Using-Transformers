import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Summarize AI",
    page_icon="◈",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;1,600&family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}
.stApp {
    background: #f8f7f4 !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 0 !important;
    padding-bottom: 48px !important;
    max-width: 700px !important;
}

/* ── Nav ── */
.topnav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 24px 0 36px;
    border-bottom: 1px solid #e8e4de;
    margin-bottom: 52px;
}
.topnav-logo {
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    color: #1a1814;
    display: flex;
    align-items: center;
    gap: 10px;
}
.topnav-badge {
    font-family: 'Inter', sans-serif;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #5b4fcf;
    background: rgba(91,79,207,0.08);
    border: 1px solid rgba(91,79,207,0.2);
    padding: 3px 8px;
    border-radius: 4px;
}
.topnav-links {
    display: flex;
    gap: 24px;
    font-size: 13px;
    color: #aaa;
    font-weight: 400;
}

/* ── Hero ── */
.hero-eyebrow {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 3.5px;
    text-transform: uppercase;
    color: #5b4fcf;
    text-align: center;
    margin-bottom: 18px;
}
.hero-h1 {
    font-family: 'Playfair Display', serif;
    font-size: 50px;
    line-height: 1.1;
    letter-spacing: -1.2px;
    color: #1a1814;
    text-align: center;
    margin: 0 0 18px;
}
.hero-h1 em {
    font-style: italic;
    color: #5b4fcf;
}
.hero-sub {
    font-size: 15px;
    color: #999;
    line-height: 1.75;
    font-weight: 300;
    text-align: center;
    margin: 0 0 44px;
}

/* ── Stats ── */
.stats-row {
    display: flex;
    border: 1px solid #e8e4de;
    border-radius: 14px;
    overflow: hidden;
    background: #fff;
    margin-bottom: 44px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.04);
}
.stat-cell {
    flex: 1;
    text-align: center;
    padding: 22px 12px;
    border-right: 1px solid #e8e4de;
}
.stat-cell:last-child { border-right: none; }
.stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 26px;
    color: #1a1814;
    line-height: 1;
    margin-bottom: 6px;
}
.stat-lbl {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #bbb;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: #fff !important;
    border: 1px solid #e8e4de !important;
    border-radius: 12px !important;
    padding: 4px !important;
    gap: 0 !important;
    margin-bottom: 16px !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.04) !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    border-radius: 9px !important;
    border: none !important;
    color: #bbb !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    padding: 11px 0 !important;
    flex: 1 !important;
    justify-content: center !important;
    transition: color 0.2s !important;
}
.stTabs [aria-selected="true"] {
    background: #5b4fcf !important;
    color: #fff !important;
}
.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-border"] { display: none !important; }

/* ── Input card ── */
.input-card {
    background: #fff;
    border: 1px solid #e8e4de;
    border-radius: 16px;
    padding: 28px;
    margin-bottom: 4px;
    box-shadow: 0 1px 6px rgba(0,0,0,0.04);
}
.input-label {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #ccc;
    margin-bottom: 12px;
}
.meta-txt {
    font-size: 12px;
    color: #ccc;
    text-align: right;
    margin-top: 8px;
}

/* ── Textarea ── */
.stTextArea textarea {
    background: #faf9f7 !important;
    border: 1px solid #e8e4de !important;
    border-radius: 10px !important;
    color: #1a1814 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    line-height: 1.7 !important;
    padding: 14px 16px !important;
}
.stTextArea textarea:focus {
    border-color: #5b4fcf !important;
    box-shadow: 0 0 0 3px rgba(91,79,207,0.1) !important;
    outline: none !important;
    background: #fff !important;
}
.stTextArea textarea::placeholder { color: #d5d0c8 !important; }

/* ── File uploader ── */
.stFileUploader > div {
    background: #faf9f7 !important;
    border: 1.5px dashed #ddd8d0 !important;
    border-radius: 10px !important;
}
.stFileUploader > div:hover {
    border-color: #5b4fcf !important;
    background: rgba(91,79,207,0.02) !important;
}
.stFileUploader label { display: none !important; }

/* ── Button ── */
.stButton > button {
    width: 100% !important;
    background: #5b4fcf !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 14px 32px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    margin-top: 16px !important;
    box-shadow: 0 4px 20px rgba(91,79,207,0.25) !important;
    letter-spacing: 0.2px !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    background: #4d42b8 !important;
    box-shadow: 0 6px 28px rgba(91,79,207,0.38) !important;
    transform: translateY(-1px) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── Result cards ── */
.res-card {
    background: #fff;
    border: 1px solid #e8e4de;
    border-radius: 14px;
    padding: 22px 24px;
    margin-top: 18px;
    box-shadow: 0 1px 6px rgba(0,0,0,0.04);
}
.res-header {
    display: flex;
    align-items: center;
    gap: 10px;
    padding-bottom: 14px;
    border-bottom: 1px solid #f0ece6;
    margin-bottom: 16px;
}
.res-icon {
    width: 30px;
    height: 30px;
    background: #5b4fcf;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    color: #fff;
    flex-shrink: 0;
}
.res-icon-teal { background: #1d9e75; }
.res-title {
    font-family: 'Playfair Display', serif;
    font-size: 16px;
    color: #1a1814;
}

/* ── Alerts ── */
.stSuccess {
    background: rgba(91,79,207,0.05) !important;
    border: 1px solid rgba(91,79,207,0.15) !important;
    border-left: 3px solid #5b4fcf !important;
    border-radius: 10px !important;
}
.stSuccess p, .stSuccess div {
    color: #3d3490 !important;
    font-size: 14px !important;
    line-height: 1.75 !important;
}
.stError {
    background: #fff5f5 !important;
    border: 1px solid rgba(220,70,70,0.2) !important;
    border-left: 3px solid #dc4646 !important;
    border-radius: 10px !important;
}
.stWarning {
    background: #fffbf0 !important;
    border: 1px solid rgba(240,180,50,0.25) !important;
    border-left: 3px solid #f0b432 !important;
    border-radius: 10px !important;
}

/* ── File meta badge ── */
.file-meta {
    font-size: 12px;
    color: #aaa;
    margin-top: 10px;
    padding: 8px 12px;
    background: #faf9f7;
    border: 1px solid #e8e4de;
    border-radius: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* ── Spinner ── */
.stSpinner > div { border-top-color: #5b4fcf !important; }

/* ── Footer ── */
.page-footer {
    text-align: center;
    padding: 44px 0 8px;
    font-size: 12px;
    color: #ccc;
}
.page-footer span { color: #5b4fcf; }
</style>
""", unsafe_allow_html=True)

# ── Nav ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="topnav">
  <div class="topnav-logo">
    ◈ NotebookRM AI
    <span class="topnav-badge">Beta</span>
  </div>
  <div class="topnav-links">
    <span>Docs</span><span>API</span><span>Sign in</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-eyebrow">AI-Powered Document Intelligence</div>
<h1 class="hero-h1">Turn any text into<br><em>clear insight</em></h1>
<p class="hero-sub">
  Paste raw text or upload a PDF — get a precise,<br>
  structured summary in seconds.
</p>
""", unsafe_allow_html=True)

# ── Stats ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-row">
  <div class="stat-cell">
    <div class="stat-num">10s</div>
    <div class="stat-lbl">Avg. Processing</div>
  </div>
  <div class="stat-cell">
    <div class="stat-num">99%</div>
    <div class="stat-lbl">Accuracy Rate</div>
  </div>
  <div class="stat-cell">
    <div class="stat-num">50 MB</div>
    <div class="stat-lbl">Max PDF Size</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab_text, tab_pdf = st.tabs(["📄  Paste Text", "📎  Upload PDF"])

# ─── Text tab ─────────────────────────────────────────────────────────────────
with tab_text:
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    st.markdown('<div class="input-label">Your content</div>', unsafe_allow_html=True)

    user_text = st.text_area(
        "text_content",
        placeholder="Paste your article, report, notes, or any text here…",
        height=260,
        label_visibility="collapsed",
    )

    words = len(user_text.split()) if user_text.strip() else 0
    st.markdown(
        f'<div class="meta-txt">{words:,} words · {len(user_text):,} chars</div>',
        unsafe_allow_html=True,
    )

    do_text = st.button("✦  Generate Summary", key="btn_text")
    st.markdown('</div>', unsafe_allow_html=True)

    if do_text:
        if not user_text.strip():
            st.warning("Please paste some text before generating a summary.")
        else:
            with st.spinner("Analysing your content…"):
                try:
                    r = requests.post(f"{BACKEND_URL}/summarize-text", data={"text": user_text})
                    if r.status_code == 200:
                        st.markdown("""
                        <div class="res-card">
                          <div class="res-header">
                            <div class="res-icon">✦</div>
                            <div class="res-title">Summary</div>
                          </div>
                        </div>""", unsafe_allow_html=True)
                        st.success(r.json()["summary"])
                    else:
                        st.error(f"Backend error: {r.text}")
                except Exception as e:
                    st.error(f"Could not connect to backend.\n\n`{e}`")

# ─── PDF tab ──────────────────────────────────────────────────────────────────
with tab_pdf:
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    st.markdown('<div class="input-label">Your document</div>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        label_visibility="collapsed",
    )

    if uploaded_file:
        kb = len(uploaded_file.getvalue()) / 1024
        size_str = f"{kb:.1f} KB" if kb < 1024 else f"{kb / 1024:.2f} MB"
        st.markdown(
            f'<div class="file-meta">'
            f'<span>📄 <strong style="color:#1a1814">{uploaded_file.name}</strong></span>'
            f'<span>{size_str}</span>'
            f'</div>',
            unsafe_allow_html=True,
        )

    do_pdf = st.button("✦  Summarize PDF", key="btn_pdf")
    st.markdown('</div>', unsafe_allow_html=True)

    if do_pdf:
        if uploaded_file is None:
            st.warning("Please upload a PDF file first.")
        else:
            with st.spinner("Extracting text and generating summary…"):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                    r = requests.post(f"{BACKEND_URL}/summarize-pdf", files=files)
                    if r.status_code == 200:
                        result = r.json()
                        st.markdown("""
                        <div class="res-card">
                          <div class="res-header">
                            <div class="res-icon">✦</div>
                            <div class="res-title">Summary</div>
                          </div>
                        </div>""", unsafe_allow_html=True)
                        st.success(result["summary"])

                        if result.get("extracted_text_preview"):
                            st.markdown("""
                            <div class="res-card">
                              <div class="res-header">
                                <div class="res-icon res-icon-teal">≡</div>
                                <div class="res-title">Extracted Text Preview</div>
                              </div>
                            </div>""", unsafe_allow_html=True)
                            st.text_area(
                                "preview",
                                value=result["extracted_text_preview"],
                                height=220,
                                label_visibility="collapsed",
                                disabled=True,
                            )
                    else:
                        st.error(f"Backend error: {r.text}")
                except Exception as e:
                    st.error(f"Could not connect to backend.\n\n`{e}`")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-footer">
  Built with Streamlit · Powered by AI · <span>Summarize AI</span>
</div>
""", unsafe_allow_html=True)