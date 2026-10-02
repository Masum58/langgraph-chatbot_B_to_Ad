from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from app.state import AgentState
from app.nodes import chat_node

def create_chatbot():
    # Initialize the Graph with AgentState
    workflow = StateGraph(AgentState)

    # Add the chatbot node
    workflow.add_node("chat_node", chat_node)

    # Define the edges: START -> chat_node -> END
    workflow.add_edge(START, "chat_node")
    workflow.add_edge("chat_node", END)

    # Add persistence with MemorySaver (checkpointer)
    checkpointer = MemorySaver()

    # Compile the graph
    return workflow.compile(checkpointer=checkpointer)

chatbot = create_chatbot()
