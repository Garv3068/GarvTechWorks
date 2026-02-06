import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Page config
st.set_page_config(
    page_title="Nexus Lite",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Nexus Lite")
st.caption("Your Campus. Simplified by AI.")

tabs = st.tabs([
    "📩 Mail Summarizer",
    "🍽️ Smart Mess Menu",
    "📚 Academic Planner"
])

# ---------------- MAIL SUMMARIZER ----------------
with tabs[0]:
    st.header("📩 AI Mail Summarizer")

    email_text = st.text_area(
        "Paste college email here",
        height=200,
        placeholder="Dear Students, This is to inform you..."
    )

    if st.button("Summarize Email"):
        if email_text.strip():
            with st.spinner("AI is summarizing..."):
                prompt = f"""
You are a campus assistant AI.

Tasks:
1. Summarize the email in ONE sentence
2. Categorize it: Exam / Event / Urgent / General
3. Extract deadline (if any)

Email:
{email_text}
"""
                response = model.generate_content(prompt)
                st.success("AI Summary")
                st.write(response.text)
        else:
            st.warning("Please paste an email.")

# ---------------- MESS MENU AI ----------------
with tabs[1]:
    st.header("🍽️ Smart Mess Menu")

    menu = st.text_area(
        "Enter today's mess menu",
        height=150,
        placeholder="Breakfast: Poha, Eggs\nLunch: Dal, Rice, Paneer\nDinner: Roti, Chicken"
    )

    if st.button("Get AI Recommendation"):
        if menu.strip():
            with st.spinner("Analyzing menu..."):
                prompt = f"""
You are a nutrition-aware campus AI.

Given this mess menu:
1. Recommend best overall meal
2. Recommend healthiest option
3. Recommend high-protein choice

Menu:
{menu}
"""
                response = model.generate_content(prompt)
                st.success("AI Recommendation")
                st.write(response.text)
        else:
            st.warning("Please enter the menu.")

# ---------------- ACADEMIC PLANNER ----------------
with tabs[2]:
    st.header("📚 Academic Planner")

    timetable = st.text_area(
        "Enter today's timetable",
        height=150,
        placeholder="9-10: Maths\n10-11: Physics\n2-3: AI Lab"
    )

    question = st.text_input(
        "Ask AI about your day",
        placeholder="Do I have free time today?"
    )

    if st.button("Ask AI"):
        if timetable.strip() and question.strip():
            with st.spinner("Thinking..."):
                prompt = f"""
You are an academic planning assistant.

Timetable:
{timetable}

Student Question:
{question}

Answer clearly and briefly.
"""
                response = model.generate_content(prompt)
                st.success("AI Answer")
                st.write(response.text)
        else:
            st.warning("Please enter timetable and question.")
