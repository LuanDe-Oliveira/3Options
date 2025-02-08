import streamlit as st

1 = st.toogle('Tem namorada')
2 = st.toogle('É bom em esportes')
3 = st.toogle('É inteligente')

if 1,2:
  3 = st.toogle('É inteligente', disabled=True)
elif 2,3:
  1 = st.toogle('Tem namorada', disabled=True)
elif 1,3:
  2 = st.toogle('É bom em esportes', disabled=True)
