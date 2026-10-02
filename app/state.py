from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    # add_messages ensures that new messages are appended to the existing list
    # rather than replacing the entire list.
    messages: Annotated[list, add_messages]
