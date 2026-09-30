import streamlit as st
from utils.prompt_optimizer import optimize_prompt, generate_demo_response

st.set_page_config(page_title="GenAI Prompt Engineering Assistant", page_icon="🤖", layout="wide")

st.markdown("""
<style>
.main-title {font-size: 38px; font-weight: 700; margin-bottom: 0;}
.subtitle {color: #666; font-size: 17px; margin-bottom: 25px;}
.card {padding: 18px; border-radius: 12px; border: 1px solid #ddd; margin-bottom: 12px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🤖 GenAI Prompt Engineering Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Transform simple requests into structured, effective prompts using prompt-engineering techniques.</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    st.subheader("1. Describe your task")
    user_request = st.text_area("Basic request", placeholder="Example: Write an email asking my manager for two days of leave.", height=150)
    role = st.selectbox("AI Role", ["Expert Assistant", "Teacher", "Software Engineer", "Data Analyst", "Content Writer", "Business Consultant"])
    tone = st.selectbox("Tone", ["Professional", "Friendly", "Concise", "Formal", "Creative", "Academic"])
with col2:
    st.subheader("2. Specify the output")
    output_format = st.selectbox("Output format", ["Bullet points", "Paragraph", "Step-by-step", "Table", "Email", "Code", "JSON"])
    audience = st.text_input("Target audience", placeholder="Example: College student / Manager / Customer")
    constraints = st.text_area("Constraints", placeholder="Example: Keep it under 150 words and use simple language.", height=100)

if st.button("✨ Optimize Prompt", type="primary", use_container_width=True):
    if not user_request.strip():
        st.warning("Please enter a basic request first.")
    else:
        optimized = optimize_prompt(user_request, role, tone, output_format, audience, constraints)
        st.session_state["optimized"] = optimized

if "optimized" in st.session_state:
    st.divider()
    st.subheader("3. Optimized Prompt")
    st.code(st.session_state["optimized"], language="text")

    if st.button("🚀 Generate AI Response", use_container_width=True):
        st.session_state["response"] = generate_demo_response(st.session_state["optimized"], user_request, output_format, tone)

if "response" in st.session_state:
    st.subheader("4. Generated Response")
    st.write(st.session_state["response"])

st.divider()
st.caption("Academic project — Generative AI and Prompt Engineering. The demo response mode works without an external API key; an LLM API can be connected through environment variables for production use.")
