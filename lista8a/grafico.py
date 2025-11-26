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

    px = []
    py = []

    p = sg.ponto_inflexao()
    xmin = p - 10
    xmax = p + 10
    npontos = 50
    dist = (xmax - xmin)/(npontos - 1)

    x  = xmin
    while x <= xmax:
        px.append(x)
        y = sg.y(x)
        py.append(y)
        x += dist
    df = pd.DataFrame(
        {
            "x": px,
            "y": py,
        }
    )

    st.line_chart(df, x="x", y="y")