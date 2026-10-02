import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from app.state import AgentState

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4o")

def chat_node(state: AgentState):
    """
    A simple node that takes the current state and returns the LLM's response.
    """
    response = llm.invoke(state["messages"])
    return {"messages": [response]}
