# Project Manager Agent Skills

## GitHub Tools

### create_issue
Creates a new issue in the configured GitHub repository.
- **Inputs:**
  - `title` (string): The title of the issue.
  - `body` (string): Detailed description of the issue.
  - `labels` (list of strings, optional): List of labels for the issue (e.g., ['bug', 'enhancement']).
- **Outputs:** Success message with the URL of the created issue or an error message.

### list_open_issues
Lists all open issues in the configured repository.
- **Inputs:** None.
- **Outputs:** Formatted text containing the number, title, and URL of open issues.

### update_issue_comment
Adds a comment to an existing issue.
- **Inputs:**
  - `issue_number` (integer): The issue number.
  - `comment` (string): The comment to be added.
- **Outputs:** Success or error message.

### list_github_files
Lists files and folders in a specific directory of the GitHub repository.
- **Inputs:**
  - `directory_path` (string, optional): The directory path (e.g., 'src' or empty for root).
- **Outputs:** Formatted list of files and subdirectories found.

### read_github_file
Reads the text content of a specific file in the GitHub repository.
- **Inputs:**
  - `file_path` (string): The full path of the file (e.g., 'src/main.py' or 'README.md').
- **Outputs:** The content of the file or an error message.

## Google Drive Tools

### list_drive_documents
Lists the 10 most recent documents available in the agent's Google Drive.
- **Inputs:** None.
- **Outputs:** A list of files with their IDs and names, or an error message.

### read_drive_document
Reads the content of a Google Drive document.
- **Inputs:**
  - `doc_id` (string): The ID of the document in Google Drive.
- **Outputs:** The text content of the document.

### save_local_document
Saves a planning document locally in the project's 'outputs' folder.
- **Inputs:**
  - `name` (string): The title of the document.
  - `content` (string): The content to be saved.
- **Outputs:** Message indicating success and the path of the generated file.
