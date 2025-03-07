from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, tool
from langchain_community.tools import TavilySearchResults

import datetime
from dotenv import load_dotenv
load_dotenv()

@tool
def current_time(format = "%Y-%m-%d %H:%M:%S"):
    """
    Returen the current date and time in the specified format
    
    """
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time


llm = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")
search_tool = TavilySearchResults(search_depth= "basic")
agent = initialize_agent(tools = [search_tool], llm=llm, agent = "zero-shot-react-description", verbose = True)
agent.invoke('give me latest 2 news happening in U.S.A')

