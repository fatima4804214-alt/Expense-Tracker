col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Add Expense"):
        if category == "":
            st.warning("Please enter category")
        else:
            date_time = datetime.now().strftime("%d %b %Y | %I:%M %p")
            stack.push((category, amount, date_time))
            st.success("Added: " + category + " - " + str(amount) + " on " + date_time)

with col2:
    if st.button("Undo Last"):
        removed = stack.pop()
        if removed:
            st.info("Removed: " + removed[0] + " - " + str(removed[1]))
        else:
            st.warning("No expense to undo")

with col3:
    if st.button("Reset All"):
        stack.stack = []
        st.warning("All expenses cleared!")
