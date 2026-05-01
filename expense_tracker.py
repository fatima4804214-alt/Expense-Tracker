# Expense Tracker using Stack + Streamlit Dashboard
# Run with: streamlit run expense_tracker.py

import streamlit as st
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime  # ✅ DATE KE LIYE ADD KIYA

# -----------------------------
# STACK CLASS
# -----------------------------
class ExpenseStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def get_all(self):
        return self.stack

# -----------------------------
# APP SETUP
# -----------------------------
st.set_page_config(page_title="Expense Tracker", layout="centered")
st.title("💰 Expense Tracker (Stack + Streamlit)")

if "stack" not in st.session_state:
    st.session_state.stack = ExpenseStack()

stack = st.session_state.stack

# -----------------------------
# INPUT SECTION
# -----------------------------
st.subheader("➕ Add Expense")

category = st.text_input("Category (e.g. Food, Travel)")
amount = st.number_input("Amount", min_value=0.0, step=1.0)

col1, col2 = st.columns(2)

with col1:
    if st.button("Add Expense"):
        if category == "":
            st.warning("Please enter category")
        else:
            date_today = datetime.now().strftime("%d %b %Y")  # ✅ e.g. 01 May 2025
            stack.push((category, amount, date_today))  # ✅ date bhi save ho rhi
            st.success(f"Added: {category} - {amount} on {date_today}")

with col2:
    if st.button("↩️ Undo Last"):
        removed = stack.pop()
        if removed:
            st.info(f"Removed: {removed[0]} - {removed[1]} ({removed[2]})")
        else:
            st.warning("No expense to undo")

# -----------------------------
# DISPLAY EXPENSES
# -----------------------------
st.subheader("📂 Expenses List")

all_items = stack.get_all()

if all_items:
    for i, item in enumerate(reversed(all_items), 1):
        st.write(f"{i}. 📅 {item[2]} | {item[0]} — Rs. {item[1]}")  # ✅ date show ho rhi
else:
    st.write("No expenses added yet.")

# -----------------------------
# TOTAL
# -----------------------------
st.subheader("💰 Total Expense")
total = sum(item[1] for item in all_items)
st.metric("Total", f"Rs. {total}")

# -----------------------------
# GRAPH
# -----------------------------
st.subheader("📊 Category-wise Graph")

data = defaultdict(float)
for cat, amt, date in all_items:  # ✅ date bhi unpack ho rhi
    data[cat] += amt

if data:
    fig, ax = plt.subplots()
    ax.bar(data.keys(), data.values())
    ax.set_xlabel("Category")
    ax.set_ylabel("Amount")
    ax.set_title("Expenses Breakdown")
    st.pyplot(fig)
else:
    st.info("No data for graph")
else:
    st.info("No data for graph")
