# LangGraph Chatbot

A step-by-step chatbot built with LangGraph. Features are added phase by phase.

## Roadmap (build ONE phase at a time)
1. [x] Simple chatbot: single node, conversation history stored in State
2. [ ] RAG over my documents
3. [ ] Tools (actions the chatbot can take)
4. [ ] UI + LangSmith tracing
5. [ ] Memory/persistence (checkpointers), human-in-the-loop, retry/fault tolerance

Current phase: 1b - checkpointer inspection and time travel
(get_state, get_state_history, replay from a checkpoint)

## Stack
- Python 3.11, LangGraph, LangChain
- LLM: OpenAI via ChatOpenAI (key in .env as OPENAI_API_KEY)
- UI: Streamlit (from Phase 4)
- Tracing: LangSmith (from Phase 4)

## Project structure
- `app/state.py`   -> State definition
- `app/nodes.py`   -> node functions
- `app/graph.py`   -> graph building and compile
- `app/cli.py`     -> terminal chat loop (entry point)
- `.env`           -> API keys (never commit)
- `.env.example`   -> template for .env
- `requirements.txt`

## Code rules
- State is a TypedDict; messages use the `add_messages` reducer
- Each node is its own function with type hints
- Never hardcode secrets; load from `.env`
- Checkpointer is in-memory for now (data is lost when the program stops)
- Keep functions small; no unrequested refactors or extra features

## Commands
- Install: `pip install -r requirements.txt`
- Run: `python -m app.cli`

## Git conventions
- Branch names: `feature/<short-name>`; never work directly on `main`
- Commit messages: `feat:`, `fix:`, `docs:`, `refactor:` prefix

## How to work with me
- Before coding a new feature, propose a short plan and wait for approval
- Do only the current phase; do not jump ahead
- After each change, tell me how to run and test it
- I am learning LangGraph: explain concepts to me in Bengali, using English technical terms, with a short practical analogy