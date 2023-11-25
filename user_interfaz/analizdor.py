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

# Streamlit app
def main():
    st.set_page_config(layout="wide")
    #st.title("Análisis de Preguntas de Historia")
    #st.write("Este gráfico muestra la distribución de temas en las preguntas de historia por usuario.")

    # Mostrar el gráfico en Streamlit
    #grafico = mostrar_grafico()
    #st.pyplot(grafico)

    data_ciencias = """
    {
    "davidgut@gmail.com": [
        {
            "pregunta": "¿Por qué es importante el ciclo del agua?",
            "categoría": "Conceptos",
            "análisis": "El estudiante está buscando entender la importancia del ciclo del agua.",
            "recomendación": "Explicar la importancia del ciclo del agua en la vida en la Tierra."
        },
        {
            "pregunta": "¿Cómo influyen las estaciones del año en el clima?",
            "categoría": "Conceptos",
            "análisis": "El estudiante está interesado en cómo las estaciones del año afectan el clima.",
            "recomendación": "Describir cómo las estaciones del año influyen en los cambios climáticos."
        },
        {
            "pregunta": "¿Qué son los ecosistemas y qué tipos existen?",
            "categoría": "Conceptos",
            "análisis": "El estudiante está buscando información sobre los ecosistemas y sus tipos.",
            "recomendación": "Definir qué es un ecosistema y describir los diferentes tipos de ecosistemas."
        },
        {
            "pregunta": "¿Qué es la energía y qué tipos de energía hay?",
            "categoría": "Conceptos",
            "análisis": "El estudiante está interesado en la energía y sus diferentes tipos.",
            "recomendación": "Definir qué es la energía y describir los diferentes tipos de energía."
        }
    ],
    "nakada2130@gmail.com": [
        {
            "pregunta": "¿Cuál es la función de las raíces en las plantas?",
            "categoría": "Biología",
            "análisis": "El estudiante está buscando información sobre la función de las raíces en las plantas.",
            "recomendación": "Explicar la función de las raíces en las plantas."
        },
        {
            "pregunta": "¿Cómo afecta la contaminación al medio ambiente?",
            "categoría": "Medio ambiente",
            "análisis": "El estudiante está interesado en cómo la contaminación afecta al medio ambiente.",
            "recomendación": "Describir los efectos de la contaminación en el medio ambiente."
        },
        {
            "pregunta": "¿Qué son los minerales y cómo se forman?",
            "categoría": "Geología",
            "análisis": "El estudiante está buscando información sobre los minerales y su formación.",
            "recomendación": "Definir qué son los minerales y explicar cómo se forman."
        }
    ],
    "personalmperez@gmail.com": [
        {
            "pregunta": "¿Qué son los fósiles y cómo nos ayudan a entender el pasado?",
            "categoría": "Paleontología",
            "análisis": "El estudiante está interesado en los fósiles y su utilidad para entender el pasado.",
            "recomendación": "Explicar qué son los fósiles y cómo nos ayudan a entender la historia de la vida en la Tierra."
        },
        {
            "pregunta": "¿Cómo se clasifican los seres vivos?",
            "categoría": "Biología",
            "análisis": "El estudiante está buscando información sobre la clasificación de los seres vivos.",
            "recomendación": "Describir cómo se clasifican los seres vivos."
        },
        {
            "pregunta": "¿Qué es la fotosíntesis?",
            "categoría": "Biología",
            "análisis": "El estudiante está interesado en la fotosíntesis.",
            "recomendación": "Explicar qué es la fotosíntesis y por qué es importante."
        }
    ],
    "mapearse.mide@gmail.com": [
        {
            "pregunta": "¿Qué son los planetas y cuáles son del sistema solar?",
            "categoría": "Astronomía",
            "análisis": "El estudiante está buscando información sobre los planetas y el sistema solar.",
            "recomendación": "Definir qué es un planeta y enumerar los planetas del sistema solar."
        },
        {
            "pregunta": "¿Cómo funciona el sistema digestivo humano?",
            "categoría": "Biología",
            "análisis": "El estudiante está interesado en el funcionamiento del sistema digestivo humano.",
            "recomendación": "Describir cómo funciona el sistema digestivo humano."
        },
        {
            "pregunta": "¿Qué es un hábitat y por qué es importante para los animales?",
            "categoría": "Ecología",
            "análisis": "El estudiante está buscando entender qué es un hábitat y su importancia para los animales.",
            "recomendación": "Definir qué es un hábitat y explicar por qué es importante para los animales."
        }
    ]
}
"""

    data_historia = """
    {
    "davidgut@gmail.com": [
        {
            "pregunta": "¿Cuáles fueron las causas de la Primera Guerra Mundial?",
            "categoría": "Causas",
            "análisis": "El estudiante está interesado en las causas de la Primera Guerra Mundial.",
            "recomendación": "Describir los factores que llevaron a la Primera Guerra Mundial."
        },
        {
            "pregunta": "¿Qué importancia tuvo Cristóbal Colón en la historia?",
            "categoría": "Personajes",
            "análisis": "El estudiante está buscando entender la importancia de Cristóbal Colón en la historia.",
            "recomendación": "Explicar el papel de Cristóbal Colón en la historia y su impacto en el mundo."
        },
        {
            "pregunta": "¿Qué fue el Renacimiento y por qué fue importante?",
            "categoría": "Periodos",
            "análisis": "El estudiante está interesado en el Renacimiento y su importancia.",
            "recomendación": "Describir las características del Renacimiento y su importancia en la historia."
        },
        {
            "pregunta": "¿Cómo era la vida en el Antiguo Egipto?",
            "categoría": "Cultura",
            "análisis": "El estudiante está buscando información sobre la vida en el Antiguo Egipto.",
            "recomendación": "Proporcionar detalles sobre la vida cotidiana, la cultura y la sociedad en el Antiguo Egipto."
        }
    ],
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
    ],
    "personalmperez@gmail.com": [
        {
            "pregunta": "¿Qué causó la caída del Imperio Romano?",
            "categoría": "Causas",
            "análisis": "El estudiante está interesado en las causas de la caída del Imperio Romano.",
            "recomendación": "Describir los factores que llevaron a la caída del Imperio Romano."
        },
        {
            "pregunta": "¿Cómo influyó la Revolución Francesa en el mundo?",
            "categoría": "Consecuencias",
            "análisis": "El estudiante está buscando entender la influencia de la Revolución Francesa en el mundo.",
            "recomendación": "Explicar cómo la Revolución Francesa cambió el mundo en términos políticos y sociales."
        },
        {
            "pregunta": "¿Qué es la Edad Media y cuáles fueron sus características principales?",
            "categoría": "Periodos",
            "análisis": "El estudiante está interesado en la Edad Media y sus características principales.",
            "recomendación": "Describir las características principales de la Edad Media."
        }
    ],
    "mapearse.mide@gmail.com": [
        {
            "pregunta": "¿Quiénes fueron los vikingos y por qué son famosos?",
            "categoría": "Personajes",
            "análisis": "El estudiante está buscando información sobre los vikingos y su fama.",
            "recomendación": "Explicar quiénes fueron los vikingos y por qué son famosos en la historia."
        },
        {
            "pregunta": "¿Qué sucedió en la Revolución Americana?",
            "categoría": "Eventos",
            "análisis": "El estudiante está interesado en los eventos de la Revolución Americana.",
            "recomendación": "Proporcionar un resumen de los eventos clave de la Revolución Americana."
        },
        {
            "pregunta": "¿Cuál fue el papel de las mujeres en la Segunda Guerra Mundial?",
            "categoría": "Personajes",
            "análisis": "El estudiante está buscando entender el papel de las mujeres en la Segunda Guerra Mundial.",
            "recomendación": "Describir el papel y las contribuciones de las mujeres durante la Segunda Guerra Mundial."
        }
    ]
}
"""

    st.title("Análisis de Preguntas de Ciencias")
    presenta_analisis(data_ciencias)
    st.title("Análisis de Preguntas de Historia")
    presenta_analisis(data_historia)
if __name__ == "__main__":
    main()