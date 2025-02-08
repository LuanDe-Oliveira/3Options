import streamlit as st

a = st.toogle('Tem namorada')
b = st.toogle('É bom em esportes')
c = st.toogle('É inteligente')

if a,b:
  c = st.toogle('É inteligente', disabled=True)
elif b,c:
  a = st.toogle('Tem namorada', disabled=True)
elif a,c:
  b = st.toogle('É bom em esportes', disabled=True)
