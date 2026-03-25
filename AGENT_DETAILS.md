# Detailed Agent Documentation

This document provides an in-depth look at the personas, instructions, and capabilities of the agents developed throughout this study.

---

## [M01] Especialista em Software (Senior SE)
**Module**: `m01_first_agent`

- **Persona**: Senior Software Engineer assisted by AI.
- **Core Instruction**: For any technical query, the agent must perform a web search to ground its response in official documentation or GitHub discussions.
- **Output Format**: Detailed Markdown reports or step-by-step tutorials.
- **Tools**: 
    - `GoogleSearchTool`: Real-time web access.

---

## [M02] Gerente de Projetos (PM/PO)
**Module**: `m02_custom_tools`

- **Persona**: Senior Project Manager / Product Owner.
- **Core Instruction**: Act as a bridge between Business (Google Drive) and Engineering (GitHub). Sincronize requirements with issues and repository files.
- **Strategy**:
    1. Read context from Drive.
    2. Analyze repo files.
    3. Synchronize with GitHub Issues.
    4. Save final plans locally.
- **Tools**:
    - **GitHub**: `create_issue`, `list_open_issues`, `update_issue_comment`, `list_github_files`, `read_github_file`.
    - **Google Drive**: `list_drive_documents`, `read_drive_document`.
    - **Local**: `save_local_document`.

---

## [M03] Tech Lead & Multi-Agent Team
**Module**: `m03_multi_agent_systems`

### Tech Lead (Orchestrator)
- **Role**: Receives high-level requirements and delegates to specialists.
- **Workflow**: Orchestrates the interaction between Coder, Reviewer, and QA.

### Sub-Agents (Specialists)
- **Coder Agent**: Expert SE focused on writing clean, functional Python code.
- **Reviewer Agent**: Senior Security & Performance expert. Adheres to PEP 8.
- **Test Agent (QA)**: Automation engineer generating `pytest` suites for coverage.

---

## [M04] Complex Workflow Agents
**Module**: `m04_complex_workflows`

This module uses a routing pattern to direct users based on their intent.

- **Router Agent**: Classifies intent into `NEW_PROJECT` or `NEW_FEATURE`.
- **Ideation Expert**: Handles `NEW_PROJECT` by defining scope, actors, and value props.
- **Feature Analyst**: Handles `NEW_FEATURE` by assessing impact on existing systems.
- **SWEBOK Auditor**: The final convergence point. Generates a formal Technical Specification based on the *Software Requirements* and *Software Design* KAs of SWEBOK V4.

---

## [M05] Assistente com Memória
**Module**: `m05_memory`

- **Persona**: Highly capable personal assistant with contextual awareness.
- **Core Instruction**: Use the current session history and historical data to provide personalized help.
- **Special Feature**: Uses standard session buffer and a specific memory retrieval tool.
- **Tools**:
    - `load_memory_tool`: Accesses past session interactions.

---
*Return to [README.md](./README.md)*
