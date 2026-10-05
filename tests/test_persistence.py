import pytest
from app.graph import chatbot
from langchain_core.messages import HumanMessage

def test_time_travel():
    config = {"configurable": {"thread_id": "test_time_travel"}}

    # 1. First interaction
    chatbot.invoke({"messages": [HumanMessage(content="Hello!")]}, config=config)
    # 2. Second interaction
    chatbot.invoke({"messages": [HumanMessage(content="I love LangGraph")]}, config=config)

    # Check history length (should have checkpoints for both)
    history = list(chatbot.get_state_history(config))
    assert len(history) >= 2

    # Get the first checkpoint (index -1 or 0 depending on order, get_state_history is usually reverse chronological)
    # Usually history[0] is the latest, history[-1] is the oldest
    oldest_state = history[-1]
    oldest_config = oldest_state.config

    # 3. Replay from oldest
    chatbot.invoke(None, config=oldest_config)

    # Verify current state now reflects only the first message
    current_state = chatbot.get_state(oldest_config)
    assert len(current_state.values["messages"]) == 2 # 1 human + 1 ai response
