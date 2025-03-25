from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import tool, create_react_agent 
from langchain_community.tools import TavilySearchResults
from langchain import hub
import datetime

import datetime
from dotenv import load_dotenv
load_dotenv()


search_tool = TavilySearchResults()
llm = ChatGoogleGenerativeAI("gemini-1.5-pro")
@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time

tools = [search_tool, get_system_time]

react_prompt = hub.pull("hwchase17/react")

react_agent_runnable = create_react_agent(tools = tools, llm=llm, prompt=react_prompt)
