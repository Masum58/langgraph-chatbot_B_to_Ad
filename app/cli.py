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

        try:
            # Invoke the chatbot with the user message and the thread config
            response = chatbot.invoke(
                {"messages": [HumanMessage(content=user_input)]},
                config=config
            )

            # The result contains the full message list; we only need the last one
            last_message = response["messages"][-1]
            print(f"AI: {last_message.content}")
        except KeyError as e:
            print(f"Configuration Error: {e}")
            break
        except Exception as e:
            # Specifically catch API errors or other failures to prevent traceback
            if "OPENAI_API_KEY" in str(e) or "Missing credentials" in str(e):
                print("\n❌ Error: OpenAI API key is missing or invalid. Please check your .env file.")
            else:
                print(f"\n❌ An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    main()
