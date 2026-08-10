import time
import streamlit as st
from reviewer import analyze_code

# Page configuration
st.set_page_config(
    page_title="AI Code Reviewer & Bug Finder", 
    page_icon="🤖", 
    layout="wide"
)

# Custom CSS for high-end SaaS look
st.markdown("""
    <style>
    .stButton button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stTextArea textarea {
        font-family: 'Courier New', Courier, monospace;
        background-color: #161b22;
        color: #c9d1d9;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.title("🤖 AI Code Reviewer & Auditor")
st.markdown("Elevate your codebase with deep AI analysis, security vulnerability checks, and automated performance optimization.")

# Sidebar Configurations
st.sidebar.header("⚙️ Audit Settings")
language = st.sidebar.selectbox(
    "Programming Language", 
    ["Python", "JavaScript", "C++", "Java", "TypeScript", "Other"]
)
persona = st.sidebar.selectbox(
    "AI Reviewer Persona", 
    [
        "Clean Code Mentor", 
        "Strict Security Auditor", 
        "Performance Expert"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🌟 System Status")
st.sidebar.success("● Llama 3 Engine Online")
st.sidebar.info("💡 **Tip:** Use **Strict Security Auditor** for finding backend vulnerabilities.")

# Main Layout (Two Columns)
col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("📝 Code Input")
    code_input = st.text_area(
        "Paste your source code below...", 
        height=500, 
        placeholder="def calculate_total(price, tax):\n    return price + tax"
    )
    analyze_btn = st.button("Run Deep Analysis 🚀", type="primary", use_container_width=True)

with col2:
    st.subheader("🔍 AI Audit & Suggestions")
    
    if analyze_btn:
        if not code_input.strip():
            st.warning("⚠️ Please provide some code in the editor before running the analysis!")
        else:
            start_time = time.time()
            
            with st.spinner(f"Running audit with {persona}... 🧐"):
                result = analyze_code(code_input, language, persona)
                
            duration = round(time.time() - start_time, 2)
            
            # Metrics Dashboard Row
            m_col1, m_col2, m_col3 = st.columns(3)
            m_col1.metric("⚡ Latency", f"{duration}s")
            m_col2.metric("📊 Language", language)
            m_col3.metric("📝 Lines", len(code_input.splitlines()))
            
            st.markdown("---")
            
            # Organized Tabs for Output
            tab1, tab2 = st.tabs(["📋 Detailed Review Report", "📥 Actions & Export"])
            
            with tab1:
                st.markdown(result)
                
            with tab2:
                st.success("✅ Audit completed successfully!")
                st.markdown("You can download the full markdown report to share with your team or save it to your repository documentation.")
                st.download_button(
                    label="📥 Download Markdown Report (.md)",
                    data=result,
                    file_name="code_review_report.md",
                    mime="text/markdown",
                    use_container_width=True
                )
    else:
        # Placeholder container when idle
        with st.container(border=True):
            st.markdown("### 👋 Ready to Review")
            st.markdown("1. Paste your code snippet on the left panel.\n2. Choose your preferred programming language and AI persona.\n3. Click **'Run Deep Analysis'** to generate a comprehensive breakdown.")