# ifrs_quiz.py
import streamlit as st

questions = [
    {
        "question": "IFRS 1 relates to:",
        "options": ["A. Insurance contracts", "B. First-time adoption", "C. Borrowing costs", "D. Revenue"],
        "answer": "B"
    },
    {
        "question": "IFRS 2 is about:",
        "options": ["A. Inventory", "B. Employee benefits", "C. Share-based payment", "D. Tax"],
        "answer": "C"
    },
    {
        "question": "Which standard governs business combinations?",
        "options": ["A. IFRS 3", "B. IAS 1", "C. IFRS 9", "D. IFRS 15"],
        "answer": "A"
    },
    {
        "question": "IFRS 9 deals with:",
        "options": ["A. Property", "B. Financial instruments", "C. Intangible assets", "D. Leases"],
        "answer": "B"
    },
    {
        "question": "Which IFRS governs revenue from contracts with customers?",
        "options": ["A. IFRS 15", "B. IFRS 16", "C. IAS 18", "D. IAS 7"],
        "answer": "A"
    },
    {
        "question": "Leases are covered under:",
        "options": ["A. IFRS 15", "B. IFRS 16", "C. IAS 17", "D. IAS 38"],
        "answer": "B"
    },
    {
        "question": "IFRS 17 relates to:",
        "options": ["A. Financial instruments", "B. Intangible assets", "C. Insurance contracts", "D. Agriculture"],
        "answer": "C"
    },
    {
        "question": "IAS 1 deals with:",
        "options": ["A. Inventory", "B. Presentation of financial statements", "C. Cash flows", "D. Tax"],
        "answer": "B"
    },
    {
        "question": "IAS 2 provides guidance on:",
        "options": ["A. Agriculture", "B. Inventory", "C. Deferred tax", "D. PPE"],
        "answer": "B"
    },
    {
        "question": "Which standard governs statement of cash flows?",
        "options": ["A. IAS 7", "B. IAS 1", "C. IFRS 10", "D. IAS 12"],
        "answer": "A"
    },
    {
        "question": "Accounting policies and errors are covered in:",
        "options": ["A. IAS 1", "B. IAS 8", "C. IAS 16", "D. IFRS 3"],
        "answer": "B"
    },
    {
        "question": "Events after the reporting period are defined in:",
        "options": ["A. IAS 12", "B. IAS 10", "C. IAS 2", "D. IAS 36"],
        "answer": "B"
    },
    {
        "question": "Which IAS covers income taxes?",
        "options": ["A. IAS 10", "B. IFRS 9", "C. IAS 12", "D. IFRS 16"],
        "answer": "C"
    },
    {
        "question": "IAS 16 governs:",
        "options": ["A. Employee benefits", "B. Intangible assets", "C. Property, Plant and Equipment", "D. Financial instruments"],
        "answer": "C"
    },
    {
        "question": "Employee benefits are handled under:",
        "options": ["A. IAS 19", "B. IAS 38", "C. IAS 2", "D. IFRS 2"],
        "answer": "A"
    },
    {
        "question": "IAS 21 focuses on:",
        "options": ["A. Leases", "B. Foreign exchange", "C. Provisions", "D. Revenue"],
        "answer": "B"
    },
    {
        "question": "Borrowing costs are regulated by:",
        "options": ["A. IFRS 7", "B. IAS 23", "C. IFRS 9", "D. IAS 28"],
        "answer": "B"
    },
    {
        "question": "Which standard requires related party disclosures?",
        "options": ["A. IFRS 12", "B. IAS 24", "C. IAS 21", "D. IAS 38"],
        "answer": "B"
    },
    {
        "question": "Which IAS addresses investments in associates?",
        "options": ["A. IAS 27", "B. IAS 28", "C. IFRS 10", "D. IAS 19"],
        "answer": "B"
    },
    {
        "question": "Which standard covers impairment of assets?",
        "options": ["A. IAS 36", "B. IFRS 9", "C. IAS 12", "D. IFRS 5"],
        "answer": "A"
    },
    {
        "question": "IAS 37 deals with:",
        "options": ["A. Provisions and contingencies", "B. Revenue", "C. PPE", "D. Leases"],
        "answer": "A"
    },
    {
        "question": "Which IAS governs intangible assets?",
        "options": ["A. IAS 16", "B. IAS 38", "C. IFRS 15", "D. IFRS 3"],
        "answer": "B"
    },
    {
        "question": "Investment properties are covered under:",
        "options": ["A. IAS 40", "B. IFRS 9", "C. IAS 12", "D. IFRS 16"],
        "answer": "A"
    },
    {
        "question": "Which IAS deals with agriculture and biological assets?",
        "options": ["A. IAS 36", "B. IAS 41", "C. IFRS 17", "D. IAS 8"],
        "answer": "B"
    }
]

st.set_page_config(page_title="IFRS Quiz", page_icon="??")
st.title("?? IFRS Quiz Application")
st.markdown("Test your knowledge of international financial reporting standards!")

score = 0
user_answers = []

for idx, q in enumerate(questions):
    st.subheader(f"Question {idx + 1}: {q['question']}")
    selected = st.radio("Choose one:", q["options"], key=idx, index=None)
    user_answers.append((selected, q["answer"]))

if st.button("Submit Quiz"):
    for i, (selected, correct) in enumerate(user_answers):
        if selected.startswith(correct):
            score += 1
    st.success(f"? You scored: {score} / {len(questions)}")
    if score == len(questions):
        st.balloons()
        st.info("?? Excellent! You mastered this set.")
    elif score >= 20:
        st.info("?? Good job! Review and try again.")
    else:
        st.warning("?? Keep practicing!")
