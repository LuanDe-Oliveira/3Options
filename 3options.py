import streamlit as st

a = st.toogle('Tem namorada')
b = st.toogle('É bom em esportes')
c = st.toogle('É inteligente')

if a and b:
    c = st.toogle('É inteligente', value=False, disabled=True)
elif b and c:
    a = st.toogle('Tem namorada', value=False, disabled=True)
elif a and c:
    b = st.toogle('É bom em esportes', value=False, disabled=True)
