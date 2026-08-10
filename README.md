# 🤖 AI-Powered Code Reviewer & Auditor

An enterprise-grade, multi-language code review and security auditing web application powered by **Groq (Llama 3)** and built with **Streamlit**. 

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- **Multi-Language Support:** Analyzes code written in Python, C++, JavaScript, Java, TypeScript, and more.
- **AI Reviewer Personas:** Switch between specialized auditing styles:
  - 🧠 **Clean Code Mentor:** Focuses on PEP 8 standards, readability, and design patterns.
  - 🛡️ **Strict Security Auditor:** Scans for SQL injections, hardcoded credentials, and vulnerabilities.
  - ⚡ **Performance Expert:** Identifies bottlenecks, time complexity issues, and memory leaks.
- **Interactive Metrics Dashboard:** Tracks response latency, lines of code, and language detection in real-time.
- **Markdown Export:** Download comprehensive audit and review reports instantly as `.md` files.

---

## 🛠️ Tech Stack

- **Frontend & UI:** Streamlit (Custom Dark-themed SaaS UI)
- **AI Engine:** Groq API (`llama-3.3-70b-versatile`)
- **Language:** Python

---

## 🚀 Getting Started Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/Irtaza-Ghafoor/Ai-Code-Reviewer.git](https://github.com/Irtaza-Ghafoor/Ai-Code-Reviewer.git)
cd Ai-Code-Reviewer
```

1. **Install Dependencies: **
pip install -r requirements.txt

2. **Set Up Environment Variables: **
Create a .env file in the root directory and add:
GROQ_API_KEY=your_groq_api_key_here

4. **Run the Application: **
streamlit run app.py

**👨‍💻 Author: **
Irtaza Ahmed
AI/ML Engineer & Computer Science Student

