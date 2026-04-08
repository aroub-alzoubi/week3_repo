from flask import Flask, render_template, request

from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers.pydantic import PydanticOutputParser

from pydantic import BaseModel

import os

from dotenv import load_dotenv

load_dotenv()

my_var = os.getenv('Aapi_Key')

app = Flask(__name__)
llm = ChatOpenAI(model="gpt-4o", api_key=my_var)
template = """

You are an AI Task Planner. Take the following raw task list and organize it.

User Tasks:

{task_input}

Provide the response as a JSON object matching this schema:

- summary: str

- organized_tasks: list of objects with category, task_name, priority

- subtasks: list of strings

"""

prompt = ChatPromptTemplate.from_template(template)


class TaskPlan(BaseModel):

    summary: str

    organized_tasks: list[dict]

    subtasks: list[str]



parser = PydanticOutputParser(pydantic_object=TaskPlan)


chain = prompt | llm | parser

@app.route("/", methods=["GET", "POST"])

def home():

    result = None

    original = None

    if request.method == "POST":

        original = request.form["task"]

        result: TaskPlan = chain.invoke({"task_input": original})

    return render_template("index.html", original=original, result=result)

if __name__ == "__main__":

    app.run(debug=True)
 