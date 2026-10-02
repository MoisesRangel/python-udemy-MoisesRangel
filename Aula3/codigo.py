# Titulo
# campo de mensagem (input)
# quando o usuario enviar uma mensagem
    # mostrar a mensagem na conversa
    # mandar a mensagem pra IA responder
    # mostrar a resposta da IA
# streamlit e openAI
#streamlit run codigo.py

import streamlit as st

st.write("## ChatBot de IA")

if not 'lista_mensagens' in st.session_state:
    st.session_state['lista_mensagens'] = []

mensagemUsuario = st.chat_input("Escreva sua mensagem aqui")

if mensagemUsuario:
    #exibir mensagem na tela
    #user -> usuario
    #assistant -> chatbot/robo/ia

    st.chat_message('user').write(mensagemUsuario)
    mensagem1 = {'role': 'user', 'content':mensagemUsuario}
    st.session_state['lista_mensagens'].append(mensagem1)

    # pegar resposta da IA
    respostaIa = 'Voce perguntou: ' + mensagemUsuario


    # enviar a mensagem da IA no chat
    st.chat_message('assistant').write(respostaIa)
    mensagem2 = {'role': 'assistant','content': respostaIa}
    st.session_state['lista_mensagens'].append(mensagem2)

# manter o historico (criar memoria)

# tornar as respostas inteligentes