import ollama
import streamlit as st

def init_session_state(keys:dict):
    for key,value in keys.items():
        if key not in st.session_state:
            st.session_state[key]=value

def chat_message_user(prompt:str)->dict:
    with st.chat_message("user"):
        st.markdown(prompt)
        return dict(role="user",content=prompt)
    
def chat_message_llm(role:str,model:str,messages:list)->dict:
    with st.chat_message(role):
        with st.spinner("대화를 생성하는 중입니다..."):
            resp=ollama.chat(model=model,messages=messages)
            msg_llm=resp.get("message",{})
            st.markdown(msg_llm["content"])
            return msg_llm
        
if __name__=="__main__":
    st.set_page_config(layout="wide")
    st.title("만들면서 배우는 챗봇")

    init_session_state(dict(msgs=[]))
    msgs: list=st.session_state["msgs"]


    for row in msgs:
        with st.chat_message(row["role"]):
            st.markdown(row["content"])

    if prompt:=st.chat_input("여기에 대화를 입력하세요."):
        msg_user=chat_message_user(prompt)
        msgs.append(msg_user)


        msg_llm=chat_message_llm("assistant",'gemma2:9b',msgs)
        msgs.append(msg_llm)

