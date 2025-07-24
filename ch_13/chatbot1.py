import ollama

message1=[{"role":"user","content":"내 이름은 파이썬이야"}]

resp1=ollama.chat(model="gemma2:9b",messages=message1)
message1.append(resp1["message"])

message1.append({"role":"user","content":"내 이름이 뭐였지?"})
resp2=ollama.chat(model="gemma2:9b",messages=message1)
message1.append(resp2["message"])

message1