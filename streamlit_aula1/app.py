import streamlit as st
import pandas as pd

st.title("Meu primeiro dash")

nome = "Davi"
idade = 18

st.subheader(nome)

st.write("Olá, mundo")
st.write("Meu nome é", nome, "e tenho", idade, "anos.")

df = pd.DataFrame({
    "Matéria": ["Português", "Matemática", "Python", "Frame"],
    "Nota": [5, 9, 7, 10]
})
st.write(df)



