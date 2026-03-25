# Google ADK Study: Building Multi-Agent Systems

This repository serves as a comprehensive study of the **Google Agent Development Kit (ADK)**, documenting the journey from creating a single AI agent to orchestrating complex, multi-agent workflows. It serves as a portfolio piece demonstrating expertise in GenAI, Agentic Workflows, and Full-Stack AI Integration.

## 🚀 Project Overview

The project is structured as a progressive learning path, with each module (`m01` to `m05`) introducing increasingly advanced concepts. It also includes **adk-web**, a sophisticated web interface for real-time interaction and debugging of the developed agents.

> [!TIP]
> **Detailed Agent Breakdown**: For a deep dive into each agent's persona, instructions, and toolsets, see [**AGENT_DETAILS.md**](./AGENT_DETAILS.md).

### 🛠️ Tech Stack

- **Backend**: Python, `google-adk`, `google-genai`, `python-dotenv`.
- **Frontend**: Angular, Material Design, SCSS.
- **Orchestration**: `concurrently` (unified startup), `GitAgent` (standardized agent definitions).
- **Tools Integrations**: Google Search, GitHub API, Google Drive API.

---

## 📂 Learning Path & Modules

### [M01] First Agent & Tooling
*   **Goal**: Zero to a functional agent.
*   **Key Skills**: System instructions, `GoogleSearchTool` integration, grounding AI responses in real-time data.
*   **Implementation**: A basic agent that can perform research and provide detailed answers based on web searches.

### [M02] Custom Tool Integration
*   **Goal**: Extending agent capabilities with bespoke APIs.
*   **Key Skills**: Implementing Python functions as tools, handling OAuth and API tokens (GitHub/Drive).
*   **Implementation**: Tools for GitHub repository management and Google Drive file operations.

### [M03] Multi-Agent Systems (MAS)
*   **Goal**: The "Agent-as-a-Tool" delegation pattern.
*   **Key Skills**: Task delegation, specialized agent roles, team orchestration.
*   **Implementation**: A complex setup where a primary agent delegates specific technical tasks to specialized sub-agents.

### [M04] Complex Workflows
*   **Goal**: Advanced orchestration patterns.
*   **Key Skills**: Routers, Sequential Chains, Loops, and Parallel Execution.
*   **Implementation**: Robust state-managed workflows that can handle non-linear logic and self-correction.

### [M05] Memory & Context
*   **Goal**: Maintaining conversational state.
*   **Key Skills**: `InMemoryRunner`, session management, contextual follow-ups.
*   **Implementation**: Agents that remember previous interactions, allowing for seamless multi-step troubleshooting.

---

## 🤖 Advanced Pattern: GitAgent

During this study, I implemented the **GitAgent** pattern to decouple agent logic from the execution runtime. This involves:
- **Declarative Definitions**: Using `agent.yaml`, `SOUL.md` (persona), and `SKILL.md` (capabilities).
- **Framework Agnosticity**: Standardizing agents so they can be exported to different runtimes (like Google ADK or others).
- **Git-Centric Workflow**: Leveraging version control for agent prompts and tool definitions, ensuring auditability and professional governance.

---

## 🌐 ADK Web Interface

A key component of this repository is the **adk-web** integration. It provides a rich UI for:
- **Real-time Chat**: Interaction with any of the defined agents.
- **Trace Debugging**: Visualizing the internal steps taken by the agents (tool calls, reasoning).
- **Artifact Management**: Viewing and managing files generated during agent interactions.

---

## 🛠️ Getting Started

### Prerequisites
- Python 3.10+
- Node.js & npm
- [Gemini API Key](https://aistudio.google.com/app/apikey)

### Installation
1.  **Clone the repo**:
    ```bash
    git clone https://github.com/luismarquitti/adk-agent.git
    cd adk-agent
    ```
2.  **Setup Environment**:
    - Copy `.env.example` to `.env` and fill in your `GEMINI_API_KEY`.
    - (Optional) Add `GITHUB_TOKEN` and `credentials.json` for M02 tools.
3.  **Install dependencies**:
    ```bash
    # Root & Backend
    python -m venv .venv
    ./.venv/Scripts/activate
    pip install -r requirements.txt
    
    # Frontend
    cd adk-web
    npm install
    ```

### Running the Project
From the root directory:
```bash
npm run dev
```
This will concurrently start the Python backend (port 8000) and the Angular frontend (port 4200).

---

## 🎓 Skills Practiced
- **Prompt Engineering**: Crafting specialized personas and system instructions.
- **Agentic Orchestration**: Designing reliable multi-step AI workflows.
- **API Integration**: Secure handling of external services and OAuth.
- **Full-Stack Development**: Connecting high-level AI logic with modern web interfaces.
- **Security Best Practices**: Decoupling secrets via environment variables and service accounts.

---
*Developed as part of my continuous study in AI Engineering.*
