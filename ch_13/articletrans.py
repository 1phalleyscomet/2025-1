import ollama
from folder import in_dir
from htmltext import extract_text_img


system_prompt=(in_dir/"system.txt").read_text(encoding="utf-8")

url="https://www.bbc.com/culture/article/20250721-intimate-images-of-the-real-hotel-california"
text,img_url=extract_text_img(url)
msg=[
    {"role":"system","content":system_prompt},
    {"role":"user","content":text}
]
resp=ollama.chat(
    model="gemma2:9b",
    messages=msg,
    options=dict(temperature=0.2),


)
msg_llm=resp.get("message",{})
msg_llm
