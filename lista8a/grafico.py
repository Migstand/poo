import streamlit as st
import pandas as pd
from equacao_seg_grau import Equacao_2_Grau

st.header("Equação do 2º Grau: a**2 + b*x + c")
a = st.text_input("Coeficiente A")
b = st.text_input("Coeficiente B")
c = st.text_input("Coeficiente C")
if st.button("Calcular"):
    sg = Equacao_2_Grau(int(a), int(b), int(c))
    st.write(sg.delta())
    st.write(sg.x1())
    st.write(sg.x2())



    df = pd.DataFrame(
        {
            "x": [-4,-3.75, -3.5, -3.25, -3, -2.5, -2, -1.5, 0, 1.5, 2, 2.5, 3, 3.25, 3.5, 3.75, 4],
            "y": [12, 10, 8, 6, 4, 2, 0, -2, -4, -2, 0, 2, 4, 6, 8, 10, 12],
        }
    )

    st.line_chart(df, x="x", y="y")