import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

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
            with st.spinner("AI is reading your mail..."):
                prompt = f"""
                Summarize this college email in one sentence.
                Categorize it (Exam / Event / Urgent / General).
                Extract deadline if any.

                Email:
                {email_text}
                """

                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )

                st.success("AI Summary")
                st.write(response.choices[0].message.content)
        else:
            st.warning("Please paste an email.")

# ---------------- MESS MENU AI ----------------
with tabs[1]:
    st.header("🍽️ Smart Mess Menu")

    menu = st.text_area(
        "Enter today's mess menu",
        placeholder="Breakfast: Poha, Eggs\nLunch: Dal, Rice, Paneer\nDinner: Roti, Chicken",
        height=150
    )

    if st.button("Get AI Recommendation"):
        if menu.strip():
            with st.spinner("Analyzing menu..."):
                prompt = f"""
                Given this mess menu:
                1. Recommend best overall meal
                2. Healthiest option
                3. High protein choice

                Menu:
                {menu}
                """

                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )

                st.success("AI Recommendation")
                st.write(response.choices[0].message.content)
        else:
            st.warning("Please enter the menu.")

# ---------------- ACADEMIC PLANNER ----------------
with tabs[2]:
    st.header("📚 Academic Planner")

    timetable = st.text_area(
        "Enter today's timetable",
        placeholder="9-10: Maths\n10-11: Physics\n2-3: AI Lab",
        height=150
    )

    question = st.text_input(
        "Ask AI about your day",
        placeholder="Do I have free time today?"
    )

    if st.button("Ask AI"):
        if timetable.strip() and question.strip():
            with st.spinner("Thinking..."):
                prompt = f"""
                Timetable:
                {timetable}

                Question:
                {question}
                """

                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )

                st.success("AI Answer")
                st.write(response.choices[0].message.content)
        else:
            st.warning("Enter timetable and question.")
