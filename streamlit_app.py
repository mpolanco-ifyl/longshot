import streamlit as st
import openai

# Autenticación con OpenAI
openai.api_key = "tu_clave_de_api_de_openai"

def generate_article(model, prompt):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Página de la aplicación
def write():
    st.title("Generador de Artículos con GPT-3")

    model = "text-davinci-002"
    title = st.text_input("Ingresa el título o tema del artículo:")
    outline = st.text_area("Ingresa el esquema generado a partir del título:")

    if st.button("Generar artículo"):
        article = generate_article(model, f"Desarrolla el siguiente esquema generado a partir del título '{title}': {outline}")
        st.success(article)

# Ejecutar la aplicación
if __name__ == "__main__":
    write()
