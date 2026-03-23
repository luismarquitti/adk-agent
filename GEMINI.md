# Gemini CLI Project Context: Google ADK Study Repository

This repository is a study workspace for the **Google Agent Development Kit (ADK)**, designed to guide developers from building a single agent to orchestrating complex, multi-agent systems.

## Project Overview

- **Purpose:** Educational repository for learning and implementing AI agents using Google's ADK.
- **Main Technologies:**
  - **Backend:** Python, `google-adk`, `google-genai`, `python-dotenv`.
  - **Frontend:** Angular, Material Design, SCSS.
  - **Orchestration:** `concurrently` (via npm) to run both backend and frontend.
- **Architecture:** A modular structure where each directory (`m01` to `m05`) represents a specific stage in the learning path.

## Key Modules

- **m01_first_agent:** Basic agent configuration with system instructions and tools like `GoogleSearchTool`.
- **m02_custom_tools:** Implementing custom functions and APIs for agents.
- **m03_multi_agent_systems:** Learning the "Agent-as-a-Tool" pattern for delegation.
- **m04_complex_workflows:** Advanced orchestration (Routers, Chains, Loops).
- **m05_memory:** Implementing conversational memory.
- **adk-web:** A rich web interface for interacting with and debugging agents.

## Building and Running

### Prerequisites

- Node.js and npm installed.
- Python 3.10+ installed.
- A virtual environment (`.venv`) set up in the root with `requirements.txt` installed.
- A `.env` file in the root containing `GEMINI_API_KEY`.

### Running the Project

From the root directory:

- **Run everything (Backend + Frontend):**
  ```bash
  npm run dev
  ```
- **Run Backend only:**
  ```bash
  npm run dev:backend
  ```
- **Run Frontend only:**
  ```bash
  npm run dev:frontend
  ```

### Manual Backend Commands

If you need to run specific ADK commands:
```bash
# Start the ADK API server
.\.venv\Scripts\adk api_server --allow_origins=http://localhost:4200 --host=0.0.0.0
```

### Manual Frontend Commands

From the `adk-web` directory:
```bash
# Install dependencies
npm install

# Start development server with backend injection
npm run serve
```

## Development Conventions

- **Agent Definition:** Agents are typically defined in an `agent.py` file within their respective module directories using the `google.adk.Agent` class.
- **Configuration:** Use `.env` files for sensitive data like API keys.
- **Frontend Assets:** Custom assets and styles are located in `adk-web/src/assets` and `adk-web/public`.
- **Backend-Frontend Connection:** The frontend uses `set-backend.js` to dynamically inject the backend API URL into its configuration during the `npm run serve` process.

## Key Files

- `package.json` (root): Global dev scripts.
- `requirements.txt` (root): Python dependencies.
- `adk-web/package.json`: Angular project configuration.
- `m01_first_agent/agent.py`: Reference implementation for a basic agent.
- `.env.example`: Template for environment variables.
