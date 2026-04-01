import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
 
load_dotenv()
 
my_var = os.getenv('Aapi_Key')
prompt = PromptTemplate(
   input_variables=["task"],
   template="Provide a detailed plan to complete this task: {task}"
)
 
llm = ChatOpenAI(
   model="gpt-4o-mini",
   temperature=0.3,
   api_key= my_var)
   
prompt_text = prompt.format(task="Finish my assignment")
result = llm.invoke(prompt_text)
print(result.content)