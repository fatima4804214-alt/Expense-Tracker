import streamlit as st
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime

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

st.set_page_config(page_title="Expense Tracker", layout="centered")
st.title("💰 Expense Tracker")

if "stack" not in st.session_state:
    st.session_state.stack = ExpenseStack()

stack = st.session_state.stack

st.subheader("➕ Add Expense")
category = st.text_input("Category (e.g. Food, Travel)")
amount = st.number_input("Amount", min_value=0.0, step=1.0)

col1, col2 = st.columns(2)

with col1:
    if st.button("Add Expense"):
        if category == "":
            st.warning("Please enter category")
        else:
            date_today = datetime.now().strftime("%d %b %Y")
            stack.push((category, amount, date_today))
            st.success("Added: " + category + " - " + str(amount) + " on " + date_today)

with col2:
    if st.button("Undo Last"):
        removed = stack.pop()
        if removed:
            st.info("Removed: " + removed[0] + " - " + str(removed[1]))
        else:
            st.warning("No expense to undo")

st.subheader("📂 Expenses List")
all_items = stack.get_all()

if all_items:
    for i, item in enumerate(reversed(all_items), 1):
        st.write(str(i) + ". " + item[2] + " | " + item[0] + " — Rs. " + str(item[1]))
else:
    st.write("No expenses added yet.")

st.subheader("💰 Total Expense")
total = 0
for item in all_items:
    total = total + item[1]
st.metric("Total", "Rs. " + str(total))

st.subheader("📊 Category-wise Graph")
data = defaultdict(float)
for item in all_items:
    data[item[0]] = data[item[0]] + item[1]

if data:
    fig, ax = plt.subplots()
    ax.bar(list(data.keys()), list(data.values()))
    ax.set_xlabel("Category")
    ax.set_ylabel("Amount")
    ax.set_title("Expenses Breakdown")
    st.pyplot(fig)
else:
    st.info("No data for graph")
