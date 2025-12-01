import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

operation = None
result = None

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Add"):
        operation = "add"
with col2:
    if st.button("Subtract"):
        operation = "subtract"
with col3:
    if st.button("Multiply"):
        operation = "multiply"
with col4:
    if st.button("Divide"):
        operation = "divide"

def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero!"
    return None

if operation:
    result = calculate(num1, num2, operation)
    if result == "Cannot divide by zero!":
        st.error(result)
    else:
        st.success(f"Result: {result}")


