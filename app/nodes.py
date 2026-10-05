import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from app.state import AgentState

# Load environment variables
load_dotenv()

# Initialize the LLM
# We wrap this in a function or check for API key to avoid crashing on import
def get_llm():
    if not os.getenv("OPENAI_API_KEY"):
        raise KeyError("OPENAI_API_KEY not found in environment variables. Please check your .env file.")
    return ChatOpenAI(model="gpt-4o")

def chat_node(state: AgentState):
    """
    A simple node that takes the current state and returns the LLM's response.
    """
    llm = get_llm()
    response = llm.invoke(state["messages"])
    return {"messages": [response]}
