import ollama
import streamlit as st
from folder import in_dir
from htmltext import extract_text_img

system_prompt=(in_dir/"system.txt").read_text(encoding="utf-8")

if __name__=="__main__":
    st.set_page_config(layout="wide")
    st.title("기사 번역 웹 앱")

    with st.form("form", border=False):
        col_url, col_submit=st.columns([9,1])
        with col_url:
            url=st.text_input(
                "text_input",
                placeholder="URL을 입력하세요.",
                label_visibility="collapsed",
            )
        with col_submit:
            submitted=st.form_submit_button("번역하기",use_container_width=True)

    if submitted:
        st.write(f"(Source){url}")
        text, img_url=extract_text_img(url)

        col_input,col_output=st.columns(2)
        with col_input:
            st.image(img_url,use_column_width=True)
            st.markdown(text)
        with col_output:
            with st.spinner("번역하는 중입니다..."):
                msgs=[
                    {"role":"system","content":system_prompt},
                    {"role":"user","content":text}
                ]
                resp=ollama.chat(
                    model="gemma2:9b",
                    messages=msgs,
                    options=dict(temperature=0.2)
                )
                msg_llm=resp.get("message",{})
                st.markdown(msg_llm["content"])