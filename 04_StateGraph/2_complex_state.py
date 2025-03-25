from typing import TypedDict
from langgraph.graph import END, StateGraph
from typing import List, TypedDict, Annotated
import operator

class simplestate(TypedDict):
    count: int
    sum: Annotated[int, operator.add]
    history: Annotated[List[int], operator.concat]


def increment(state: simplestate) -> simplestate:
    new_count = state['count'] + 1
    return {
        "count" : new_count,
        "sum" : state["sum"] + new_count,
        "history" : [new_count]
    }

def should_continue(state):
    if (state['count'] < 5):
        return "continue"
    else:
        return "stop"
    
graph = StateGraph(simplestate)


graph.add_node("increment", increment)
graph.set_entry_point("increment")
graph.add_conditional_edges("increment", 
                            should_continue,
                            {
                                "continue":"increment",
                                "stop": END
                            }
                            )

app = graph.compile()

state = {
    "count" : 0 ,
    "sum" : 0,
    "history" : []
    }

result = app.invoke(state)
print(result)