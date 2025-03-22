import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# System message template for prompt optimization
SYSTEM_MESSAGE = """
You are a professional prompt engineer. Rewrite the user's prompt for maximum effectiveness on any LLM (ChatGPT, Gemini, Claude).
Apply these principles:

1. **Explicit Intent**: Clarify the main goal (e.g., explain, create, analyze)
2. **Context/Scope**: Define boundaries (time, domain, technical level)
3. **Structured Output**: Specify format (markdown, bullets, JSON)
4. **Audience/Tone**: Set appropriate style (casual, academic, technical)
5. **Examples**: Add representative examples if needed

Use this template:
**Role**: [Expert Role]
**Task**: [Action Verb + Objective]
**Guidelines**:
- [Detail 1]
- [Detail 2]
- [Detail 3]
"""

def optimize_prompt(user_prompt, style="General"):
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_MESSAGE},
                {"role": "user", "content": f"Original prompt: {user_prompt}\nOptimization style: {style}"}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="Prompt Optimizer", layout="wide")
st.title("🦾 AI Prompt Optimizer")

# Input section
with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        user_input = st.text_area("Enter your human-written prompt:", height=150)
    with col2:
        style = st.selectbox(
            "Optimization Style:",
            ("General", "Technical", "Creative", "Academic", "Business")
        )

# Optimization button
if st.button("✨ Optimize Prompt"):
    if user_input.strip():
        with st.spinner("Optimizing your prompt..."):
            optimized = optimize_prompt(user_input, style)
            
            # Display results in tabs
            tab1, tab2 = st.tabs(["Optimized Prompt", "Explanation"])
            
            with tab1:
                st.subheader("Enhanced Prompt")
                st.code(optimized, language="markdown")
                
            with tab2:
                st.subheader("What Changed?")
                st.write("""
                - 🎯 **Sharpened Focus**: Removed ambiguity in the main objective
                - 🏗️ **Added Structure**: Organized requirements into clear sections
                - 👥 **Audience Alignment**: Adjusted tone for better accessibility
                - 📝 **Examples Included**: Added representative samples when needed
                """)
    else:
        st.warning("Please enter a prompt to optimize")

# Sidebar info
with st.sidebar:
    st.markdown("## How to Use")
    st.write("1. Enter your natural language prompt")
    st.write("2. Choose optimization style")
    st.write("3. Get LLM-ready prompt")
    st.markdown("---")
    st.markdown("**Supported LLMs:**\n- ChatGPT\n- Gemini\n- Claude")
    st.markdown("---")
    st.markdown("Built with 💪🏻 by @Sam6002 ") 