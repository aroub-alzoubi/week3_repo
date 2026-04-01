from langchain_core.tools import Tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv("Aapi_Key")
def summarize(text: str) -> str:
   llm = ChatOpenAI(model="gpt-4o-mini", api_key=key)
   response = llm.invoke(f"Summarize this text:\n{text}")
   return response.content
def count_words(text: str) -> str:
   return f"Word count: {len(text.split())}"
tools = [
   Tool(
       name="summarizer",
       func=summarize,
       description="Summarizes a given text"
   ),
   Tool(
       name="word_counter",
       func=count_words,
       description="Counts words in a given text"
   )
]
llm = ChatOpenAI(model="gpt-4o-mini", api_key=key)
agent = create_agent(llm, tools=tools)
user_input = input("Enter your text:\n")
result = agent.invoke({
   "messages": [
       {
           "role": "user",
           "content": f"Summarize this text and then count the number of words in the summary:\n{user_input}"
       }
   ]
})
print("\nAgent Result:")
print(result["messages"][-1].content)