import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def analyze_code(code_text, language, persona):
    # Yeh local aur live dono ke liye smart check hai (chahe GROQ ho ya GEMINI)
    api_key = None
    
    # 1. Pehle Streamlit Cloud secrets check karega
    try:
        if "GROQ_API_KEY" in st.secrets:
            api_key = st.secrets["GROQ_API_KEY"]
        elif "GEMINI_API_KEY" in st.secrets:
            api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

    # 2. Agar wahan na mile toh local .env se utha lega
    if not api_key:
        api_key = os.getenv("GROQ_API_KEY") or os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Error: API key not found. Please check your .env file or Streamlit secrets."

    try:
        client = Groq(api_key=api_key)
    except Exception as e:
        return f"Error initializing Groq client: {str(e)}"
    
    # Dynamic system prompt based on user's selected persona
    persona_prompts = {
        "Strict Security Auditor": "You are a paranoid Chief Information Security Officer (CISO). Focus heavily on vulnerabilities, SQL injections, hardcoded secrets, and data leaks.",
        "Performance Expert": "You are a Senior Performance & Systems Engineer. Focus primarily on time complexity, memory leaks, and execution speed bottlenecks.",
        "Clean Code Mentor": "You are a friendly Principal Software Engineer. Focus on readability, design patterns, PEP 8 standards, and maintainability."
    }
    
    system_instruction = persona_prompts.get(persona, persona_prompts["Clean Code Mentor"])
    
    prompt = f"""
    {system_instruction}
    
    Analyze the following {language} code. Provide your response in clear Markdown sections:
    
    1. **Code Quality & Summary:** Brief overview of what the code does.
    2. **Bugs & Logical Errors:** Point out any syntax, logic, or runtime errors.
    3. **Security & Performance:** Highlight security vulnerabilities or performance bottlenecks based on your persona.
    4. **Refactored/Optimized Code:** Provide the clean, corrected, and optimized version of the code in a code block.

    Here is the code:
    ```{language}
    {code_text}
    ```
    """
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"