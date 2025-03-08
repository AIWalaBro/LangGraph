from typing import List, Sequence
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
# from langchain_community.graphs import MemgraphGraph
from langgraph.graph import END, MessageGraph
from chains import generation_chain , reflection_chain

load_dotenv()


# create generate node , create reflect node 

graph = MessageGraph()

REFLECT = "reflect"
GENERATE = "generate"

# starting point of node that is generate node
def generate_node(state):
    return generation_chain.invoke({
        "messages" : state
    })

# refelction node
def reflect_node(state):
    response =  reflection_chain.invoke({
        "messages": state
    })
    return [HumanMessage(content = response.content)]

# adding nodes
graph.add_node(GENERATE, generate_node)
graph.add_node(REFLECT, reflect_node)

# setting entry points
graph.set_entry_point(GENERATE)

# edges
def should_continue(state):
    if (len(state) > 3):
        return END
    return REFLECT

graph.add_conditional_edges(GENERATE, should_continue)
graph.add_edge(REFLECT, GENERATE)

app = graph.compile()

# mermide graph
print(app.get_graph().draw_mermaid())
app.get_graph().print_ascii()


response = app.invoke(HumanMessage(content="AI Agents taking over content creation"))

print(response)

