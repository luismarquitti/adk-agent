# Module 5: Give Your Agents Memory

## Overview
Understand the critical role of conversational memory, enabling your agents to handle follow-up questions, learn from feedback, and manage multi-step tasks seamlessly.

## Configuration & Usage
This module contains an agent in `agent.py` configured with memory capabilities:
1. **Memory Buffer (Sessão Atual):** Retém o contexto pelo `include_contents="default"` interno do agente.
2. **Long-Term Memory:** Possui a tool `load_memory_tool` acessível, na qual o agente pode utilizar para recuperar informações do `InMemoryMemoryService` do ambiente, caso ativado.

### How to Test
1. Execute the backend server pointing to the agent:
   ```bash
   .\.venv\Scripts\adk api_server --allow_origins=http://localhost:4200 --host=0.0.0.0 --agent-path=m05_memory.agent:root_agent
   ```
2. In the `adk-web` interface, start a chat session. Tell the agent your name and some facts. Later in the same chat, ask the agent to recall those facts to verify the conversational memory buffer is functioning correctly.
