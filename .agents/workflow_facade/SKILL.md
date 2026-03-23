# Workflow Facade Agent Skills

## Complex Workflow Tools

### execute_swebok_workflow
Mandatory tool to be called whenever the user makes a request. It executes complex orchestration (Router -> Specialist -> SWEBOK) and returns the generated Markdown.
- **Inputs:**
  - `user_request` (string): The user's original request.
- **Outputs:** A detailed Markdown document structured according to SWEBOK V4.
