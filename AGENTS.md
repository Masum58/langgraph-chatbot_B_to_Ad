# LangGraph Chatbot

A step-by-step chatbot built with LangGraph. Features are added phase by phase.

## Roadmap (build ONE phase at a time)
1. Simple chatbot: single node, conversation history stored in State
2. RAG over my documents
3. Tools (actions the chatbot can take)
4. UI + LangSmith tracing
5. Memory/persistence (checkpointers), human-in-the-loop, retry/fault tolerance

Current phase: 1

## Stack
- Python 3.11, LangGraph, LangChain
- LLM: <your provider, e.g. OpenAI / Groq>
- UI: Streamlit (from Phase 4)
- Tracing: LangSmith (from Phase 4)

## Project structure
- `app/state.py`   -> State definition
- `app/nodes.py`   -> node functions
- `app/graph.py`   -> graph building and compile
- `tests/`         -> pytest tests
- `.env`           -> API keys (never commit)

## Code rules
- State is a TypedDict; messages use the `add_messages` reducer
- Each node is its own function with type hints
- Never hardcode secrets; load from `.env`
- Keep functions small; no unrequested refactors or extra features

## Commands
- Install: `pip install -r requirements.txt`
- Run: `python -m app.main`
- Test: `pytest -q`

## How to work with me
- Before coding a new feature, propose a short plan and wait for approval
- Do only the current phase; do not jump ahead
- After each change, run the tests and report the result
- I am learning LangGraph: explain concepts to me in Bengali, using English technical terms, with a short practical analogy