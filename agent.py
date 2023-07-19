# Agentの実験
# 自然言語で命令を与えるとGoogleとか計算ツールとかを使って自律的に行動するエージェント

# pip install google-search-results
# export SERPAPI_API_KEY="ここにSerapiのAPIキーを入れる"
from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
import os

# AI-MOPが対応してない機能を使うと普通に動かない
os.environ["OPEN_API_KEY"] = os.environ.get('INIAD_OPENAI_API_KEY')
os.environ["OPEN_API_BASE"] = "https://api.openai.iniad.org/api/v1/"


llm = OpenAI(temperature=0)
tools = load_tools(["serpapi"],llm=llm)

agent = initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)

# やってほしいことを入れる
output = agent.run("Summarize this web page: https://www.iniad.org/en/iniad/")

# 普通に英語で返ってくるので注意
print(output)
