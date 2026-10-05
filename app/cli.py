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

        # Handle special commands
        if user_input.startswith("/"):
            parts = user_input.split()
            cmd = parts[0].lower()

            if cmd == "/state":
                state = chatbot.get_state(config)
                print(f"\n--- Current State ---")
                print(f"Checkpoint ID: {state.config['configurable'].get('checkpoint_id')}")
                print(f"Next Node: {state.next}")
                print(f"Messages: {len(state.values.get('messages', []))}")
                print(f"Content: {state.values.get('messages', [])[-1].content if state.values.get('messages') else 'None'}")
                continue

            elif cmd == "/history":
                print(f"\n--- Conversation History ---")
                history = list(chatbot.get_state_history(config))
                for i, state in enumerate(history):
                    cid = state.config['configurable'].get('checkpoint_id', 'N/A')
                    msg_count = len(state.values.get('messages', []))
                    print(f"[{i}] ID: {cid[:8]}... | Next: {state.next} | Msgs: {msg_count}")
                if not history:
                    print("No history found.")
                continue

            elif cmd == "/replay":
                if len(parts) < 2:
                    print("Usage: /replay <number>")
                    continue
                try:
                    idx = int(parts[1])
                    history = list(chatbot.get_state_history(config))
                    if 0 <= idx < len(history):
                        target_state = history[idx]
                        # Replay from this checkpoint
                        replay_config = target_state.config
                        chatbot.invoke(None, config=replay_config)
                        # Update current session config to this checkpoint
                        config = replay_config
                        print(f"Rewound to checkpoint [{idx}]. Conversation reset to that point.")
                    else:
                        print(f"Invalid index. Please choose 0 to {len(history)-1}.")
                except ValueError:
                    print("Please provide a valid number for the checkpoint index.")
                continue

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
