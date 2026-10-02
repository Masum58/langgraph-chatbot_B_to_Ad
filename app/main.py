from langchain_core.messages import HumanMessage
from app.graph import chatbot

def main():
    print("Chatbot started! Type 'exit', 'quit', or 'bye' to stop.")

    # Use a fixed thread_id for the session to test memory
    thread_id = "1"
    config = {"configurable": {"thread_id": thread_id}}

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break

        # Invoke the chatbot with the user message and the thread config
        response = chatbot.invoke(
            {"messages": [HumanMessage(content=user_input)]},
            config=config
        )

        # The result contains the full message list; we only need the last one
        last_message = response["messages"][-1]
        print(f"AI: {last_message.content}")

if __name__ == "__main__":
    main()
