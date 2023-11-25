import streamlit as st


def autentication() -> bool:
    with st.sidebar:
        with st.form("registration"):
            st.write("Login")
            usuario = st.text_input("usuario")
            password = st.text_input("contraseña")
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.info("Sucessfully")
                return True
            else:
                return False
