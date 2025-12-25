
import streamlit as st
from datetime import datetime

# Função para salvar respostas
def salvar_respostas(dados):
    with open("respostas.txt", "a", encoding="utf-8") as f:
        f.write(dados + "\n")


st.title("Assistente Aywa 🤍")

st.write(
    "Olá, para eu saber que você é quem eu estava esperando,\n"
    "responda esta pergunta:"
)

respostas_validas = {
    "chocolate",
    "um chocolate",
    "uma barra de chocolate"
}

# Primeira pergunta
a = st.text_input("O que você ganhou do Lúcio na véspera de Natal?")

if a:
    a_limpo = a.strip().lower()

    if a_limpo in respostas_validas:
        st.success("Muito bem, Rosa! Bem-vinda.")

        st.write(
            "Eu me chamo Aywa, assistente virtual do Lúcio.\n"
            "Quero te fazer umas perguntas."
        )

        # Segunda pergunta
        b = st.text_input("1ª pergunta: O que você acha do Lúcio?")

        if b:
            # Terceira pergunta
            c = st.radio(
                "Se o Lúcio te convidar para tomar um sorvete ou ir a uma pizzaria, você aceita?",
                ["sim", "não"]
            )

            if st.button("Enviar respostas"):
                # Mensagem conforme resposta
                if c == "sim":
                    st.success("😊 Ô ba! Convite aceito! Vamos marcar o dia! Beijos 💖")
                else:
                    st.info("Que pena, convite recusado.")

                # Data
                data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                # Resumo na tela
                st.subheader("📋 Resumo das Respostas")

                with st.expander("Clique para ver o resumo"):
                    st.write(f"🗓 **Data:** {data}")
                    st.write(f"🎁 **Presente recebido:** {a}")
                    st.write(f"💬 **O que acha do Lúcio:** {b}")
                    st.write(f"🍕 **Aceitou o convite:** {c}")

                # Texto para salvar
                registro = (
                    f"Data: {data}\n"
                    f"Resposta 1: {a}\n"
                    f"Resposta 2: {b}\n"
                    f"Resposta 3: {c}\n"
                    f"{'-'*40}"
                )

                salvar_respostas(registro)

                st.success("Respostas salvas automaticamente ✅")

    else:
        st.error("Resposta incorreta! ❌")