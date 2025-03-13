from langgraph.prebuilt.tool_executor import ToolExecutor
from agent_reason_runnable import react_agent_runnable, tools
from react_state import AgentState
from dotenv import load_dotenv
load_dotenv()
tool_executor =ToolExecutor(tools)

def reason_node(state:AgentState):
    agent_outcome = react_agent_runnable.invoke(state)
    return {"agent_outcome": agent_outcome}



def act_node(state:AgentState):
    agent_action = state["agent_outcome"]
    output = tool_executor.invoke(agent_action)
    return{"intermediate_steps" : [(agent_action, str(output))]}