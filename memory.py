# Memoryの実験
from langchain import OpenAI, ConversationChain
import os

# AI-MOPが対応してない機能を使うと普通に動かない
os.environ["OPEN_API_KEY"] = os.environ.get('INIAD_OPENAI_API_KEY')
os.environ["OPEN_API_BASE"] = "https://api.openai.iniad.org/api/v1/"


llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

output = conversation.run("私の名前はかめさんです。よろしくね")
output = conversation.run("私は誰ですか？")

print(output)
