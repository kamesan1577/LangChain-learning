# Chainsの実験
# LangChainの持つ機能を連結して使える

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import os

# AI-MOPが対応してない機能を使うと普通に動かない
os.environ["OPEN_API_KEY"] = os.environ.get('INIAD_OPENAI_API_KEY')
os.environ["OPEN_API_BASE"] = "https://api.openai.iniad.org/api/v1/"

# モデルのインスタンスを作成
chat = ChatOpenAI(temperature=0)

# プロンプトのテンプレート文章を定義
template = PromptTemplate.from_template("""
{adjective_of_person}な人が暴言を吐くときに言いがちなことは？
""")


chain = LLMChain(llm=chat, prompt=template,verbose=True)

# 引数に入れた言葉がtemplateに入れた文章に入る
output = chain.run("バカ")
print(output)
