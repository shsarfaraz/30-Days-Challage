import streamlit as st

st.title("Simple Calculator")
num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")
operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        st.success(num1 + num2)
    elif operation == "Subtract":
        st.success(num1 - num2)
    elif operation == "Multiply":
        st.success(num1 * num2)
    elif operation == "Divide":
        if num2 != 0:
            st.success(num1 / num2)
        else:
            st.error("Cannot divide by zero")
