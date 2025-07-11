import streamlit as st
from datetime import datetime
import pandas as pd
import csv

# ------------------- CẤU HÌNH ------------------- #
DEADLINE = datetime(2025, 7, 15, 22, 0, 0)  # thời điểm đóng bài test
CSV_FILE = "results.csv"

# ------------------- DANH SÁCH CÂU HỎI ------------------- #
questions = [
    {"question": "IFRS 1 is about:", "options": ["First-time Adoption of IFRS", "Share-based Payment", "Business Combinations"], "answer": "First-time Adoption of IFRS"},
    {"question": "IFRS 2 relates to:", "options": ["Leases", "Share-based Payment", "Revenue"], "answer": "Share-based Payment"},
    {"question": "IFRS 3 covers:", "options": ["Business Combinations", "Financial Instruments", "Agriculture"], "answer": "Business Combinations"},
    {"question": "IFRS 15 is about:", "options": ["Leases", "Revenue from Contracts with Customers", "Operating Segments"], "answer": "Revenue from Contracts with Customers"},
    {"question": "IAS 2 deals with:", "options": ["Inventory", "Cash Flow", "Leases"], "answer": "Inventory"}
]

# ------------------- KIỂM TRA DEADLINE ------------------- #
now = datetime.now()
if now > DEADLINE:
    st.title("⛔ Bài kiểm tra đã đóng")
    st.info("Kết quả các thí sinh đã nộp:")
    try:
        df = pd.read_csv(CSV_FILE)
        st.dataframe(df)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Tải kết quả CSV", csv, "results.csv", "text/csv")
    except FileNotFoundError:
        st.warning("Chưa có kết quả nào được ghi nhận.")
    st.stop()

# ------------------- NHẬP THÔNG TIN THÍ SINH ------------------- #
st.title("📋 IFRS Quiz - Trắc nghiệm chuẩn mực quốc tế")
name = st.text_input("👤 Họ và tên")
phone = st.text_input("📱 Số điện thoại")

if not name or not phone:
    st.warning("Vui lòng nhập đầy đủ họ tên và số điện thoại để bắt đầu bài test.")
    st.stop()

st.success("✅ Thông tin đã được ghi nhận. Bắt đầu làm bài!")

# ------------------- HIỂN THỊ CÂU HỎI ------------------- #
st.subheader("📝 Câu hỏi")
score = 0
user_answers = []

for idx, q in enumerate(questions):
    st.write(f"**Câu {idx + 1}: {q['question']}**")
    answer = st.radio("Chọn 1 đáp án:", q['options'], key=f"q{idx}", index=None)
    user_answers.append((q['question'], answer))
    if answer == q['answer']:
        score += 1

# ------------------- NỘP BÀI ------------------- #
if st.button("📨 Nộp bài"):
    st.success(f"🎉 {name}, bạn đã làm đúng {score}/{len(questions)} câu.")

    # Ghi vào file CSV
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), name, phone, score])

    # Hiển thị lại chi tiết câu trả lời
    st.subheader("📄 Chi tiết bài làm:")
    for i, (question, answer) in enumerate(user_answers):
        correct = questions[i]['answer']
        st.write(f"{i+1}. {question}")
        st.write(f"- ✅ Đáp án đúng: {correct}")
        st.write(f"- 📝 Bạn chọn: {answer if answer else 'Không chọn'}")
        st.markdown("---")
