import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

import streamlit as st
import numpy as np

st.set_page_config(page_title="UCGR Math App", layout="wide")

st.title("🧮 UCGR Math App")
st.sidebar.title("Select an Option")

option = st.sidebar.selectbox("Choose Operation", [
    "Number System Converter", 
    "Arithmetic Operations",
    "Combinatorics", 
    "Probability", 
    "Matrix Operations",
    "Set Theory"
])

if option == "Number System Converter":
    st.subheader("Convert between Binary, Decimal, Octal, and Hexadecimal")
    number = st.text_input("Enter a number")
    base = st.selectbox("Input base", ["Binary", "Decimal", "Octal", "Hexadecimal"])
    if number:
        try:
            if base == "Binary":
                dec = int(number, 2)
            elif base == "Decimal":
                dec = int(number)
            elif base == "Octal":
                dec = int(number, 8)
            else:
                dec = int(number, 16)
            st.write("Binary:", bin(dec))
            st.write("Decimal:", dec)
            st.write("Octal:", oct(dec))
            st.write("Hexadecimal:", hex(dec))
        except ValueError:
            st.error("Invalid number for selected base")

elif option == "Arithmetic Operations":
    st.subheader("Basic Arithmetic")
    a = st.number_input("Enter first number", value=0.0)
    b = st.number_input("Enter second number", value=0.0)
    st.write("Addition:", a + b)
    st.write("Subtraction:", a - b)
    st.write("Multiplication:", a * b)
    st.write("Division:", a / b if b != 0 else "Undefined")

elif option == "Combinatorics":
    from math import factorial as fact
    st.subheader("Permutations and Combinations")
    n = st.number_input("Enter n", value=0, step=1)
    r = st.number_input("Enter r", value=0, step=1)
    if n >= r:
        st.write("nPr:", fact(n) // fact(n - r))
        st.write("nCr:", fact(n) // (fact(r) * fact(n - r)))
    else:
        st.error("Ensure n ≥ r")

elif option == "Probability":
    st.subheader("Probability Calculator")
    favorable = st.number_input("Favorable outcomes", value=0, step=1)
    total = st.number_input("Total outcomes", value=1, step=1)
    if favorable <= total:
        st.write("Probability:", favorable / total)
    else:
        st.error("Favorable outcomes cannot exceed total outcomes")

elif option == "Matrix Operations":
    st.subheader("Matrix Addition")
    rows = st.number_input("Rows", 2, 10, step=1)
    cols = st.number_input("Columns", 2, 10, step=1)
    A = []
    B = []
    st.write("Enter Matrix A")
    for i in range(rows):
        A.append([st.number_input(f"A[{i}][{j}]", key=f"a{i}{j}") for j in range(cols)])
    st.write("Enter Matrix B")
    for i in range(rows):
        B.append([st.number_input(f"B[{i}][{j}]", key=f"b{i}{j}") for j in range(cols)])
    result = np.array(A) + np.array(B)
    st.write("Result (A + B):")
    st.write(result)

elif option == "Set Theory":
    st.subheader("Basic Set Operations")
    set1 = set(st.text_input("Enter elements of Set A (comma separated)", "").split(","))
    set2 = set(st.text_input("Enter elements of Set B (comma separated)", "").split(","))
    st.write("Union:", set1 | set2)
    st.write("Intersection:", set1 & set2)
    st.write("Difference (A - B):", set1 - set2)
