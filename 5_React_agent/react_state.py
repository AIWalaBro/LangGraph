import operator
from typing import Annotated, TypedDict, Union

from langchain_core.agents import AgentAction, AgentFinish

class AgentState(TypedDict):
    input:str
    agent_outcome: Union[AgentAction, AgentAction, None]
    intermediate_steps: Annotated[list[tuple[AgentAction, AgentFinish, str]], operator.add]
    