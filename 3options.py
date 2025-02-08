import streamlit as st

# Função para controlar o comportamento dos checkboxes
def controlar_checkboxes():
    # Checkboxes
    toggle1 = st.checkbox('Toggle 1')
    toggle2 = st.checkbox('Toggle 2')
    
    # Se os dois primeiros toggles forem selecionados, desmarcar o terceiro
    if toggle1 and toggle2:
        toggle3 = False
        toggle3_disabled = True
    else:
        toggle3 = st.checkbox('Toggle 3')
        toggle3_disabled = False

    # Mostrar o terceiro checkbox
    if toggle3_disabled:
        st.write("O Toggle 3 foi desmarcado automaticamente, pois os dois primeiros foram selecionados.")
    
    return toggle1, toggle2, toggle3

# Título do app
st.title("Exemplo de Toggles com Streamlit")

# Chamada da função que verifica os checkboxes
toggle1, toggle2, toggle3 = controlar_checkboxes()

