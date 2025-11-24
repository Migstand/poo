import streamlit as st
from retangulo import Retangulo

st.header("Cálculo com Retângulo")
b = st.text_input("Infome a base")
h = st.text_input("Informe a altura")
if st.button("Calcular"):
    r = Retangulo(float(b), float(h))
    st.write(f"Área = {r.calc_area()}")
    st.write(f"Diagonal = {r.calc_diagonal()}")
    st.write(r)