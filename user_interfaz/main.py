import json
import pandas as pd
import streamlit as st
import utils

def presenta_analisis(data):
    # Convertir la cadena JSON en un diccionario
    data_dict = json.loads(data)

    # Iterar sobre cada email y crear un DataFrame para cada uno
    for email, questions in data_dict.items():
        # Preparar una lista para almacenar las filas del DataFrame
        rows = []

        # Procesar cada pregunta y añadirla a la lista de filas
        for question in questions:
            row = {
                "Pregunta": question["pregunta"],
                "Categoría": question["categoría"],
                "Análisis": question["análisis"],
                "Recomendación": question["recomendación"]
            }
            rows.append(row)

        # Crear un DataFrame de Pandas con las filas
        df = pd.DataFrame(rows)
        df.index = df.index + 1

        # Mostrar el email y el DataFrame en Streamlit
        st.write(f"Email: {email}")
        st.table(df)

st.set_page_config(layout="wide")

data = utils.get_all_conversation()

df = pd.DataFrame(data,columns=["id","username","role","conversation_id","content"])

usernames = list(df["username"].unique())
user = st.selectbox("alumnos",usernames)

conversations = list(df[df["username"]==user]["conversation_id"].unique())
conversation = st.selectbox("alumnos",conversations)

show_df = df[(df["username"]==user) & (df["conversation_id"]==conversation)]
st.write(show_df)

analizer = st.button("analize")



data_historia = """
    {
    "nakada2130@gmail.com": [
        {
            "pregunta": "¿Quién fue Leonardo da Vinci y cuáles fueron sus aportes?",
            "categoría": "Personajes",
            "análisis": "El estudiante está buscando información sobre Leonardo da Vinci y sus contribuciones.",
            "recomendación": "Describir la vida de Leonardo da Vinci y sus principales aportes a la ciencia y el arte."
        },
        {
            "pregunta": "¿Qué fue la Revolución Industrial y cómo cambió la sociedad?",
            "categoría": "Eventos",
            "análisis": "El estudiante está interesado en la Revolución Industrial y su impacto en la sociedad.",
            "recomendación": "Explicar los cambios que la Revolución Industrial trajo a la sociedad y la economía."
        },
        {
            "pregunta": "¿Cuáles fueron las principales civilizaciones de Mesoamérica?",
            "categoría": "Cultura",
            "análisis": "El estudiante está buscando información sobre las principales civilizaciones de Mesoamérica.",
            "recomendación": "Enumerar y describir las principales civilizaciones de Mesoamérica."
        }
    ]
}
"""


if analizer:
    st.title("Dashboard")

    presenta_analisis(data_historia)