import streamlit as st

a = st.toggle('Tem namorada')
b = st.toggle('É bom em esportes')
c = st.toggle('É inteligente')

if a and b:
    c = st.toggle('É inteligente', value=False, disabled=True)
elif b and c:
    a = st.toggle('Tem namorada', value=False, disabled=True)
elif a and c:
    b = st.toggle('É bom em esportes', value=False, disabled=True)
