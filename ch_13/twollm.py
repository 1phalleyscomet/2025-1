import ollama
import streamlit as st

from chatbotwebapp import(
    chat_message_llm,
    chat_message_user,
    init_session_state,
)

if __name__=="__main__":
    st.set_page_config(layout="wide")
    st.title("만들면서 배우는 챗봇2")
    init_session_state(dict(gemma=[],llama=[]))
    gemma:list=st.session_state["gemma"]
    llama:list=st.session_state["llama"]

    for msg_gemma,msg_llama in zip(gemma,llama):
        if msg_gemma["role"]=="user":
            with st.chat_message("user"):
                st.markdown(msg_gemma["content"])

        else:
            col_gemma,col_llama=st.columns(2)
            with col_gemma:
                with st.chat_message("gemma"):
                    st.markdown(msg_gemma["content"])
            with col_llama:
                with st.chat_message("llama"):
                    st.markdown(msg_llama["content"])
    if prompt :=st.chat_input("여기에 대화를 입력하세요."):
        msg_user=chat_message_user(prompt)
        gemma.append(msg_user)
        llama.append(msg_user)

        col_gemma,col_llama=st.columns(2)
        with col_gemma:
            msg_gemma=chat_message_llm("gemma","gemma2:9b",gemma)
            gemma.append(msg_gemma)
        with col_llama:
            msg_llama=chat_message_llm("llama","llama3.1:8b",llama)
            llama.append(msg_llama)                