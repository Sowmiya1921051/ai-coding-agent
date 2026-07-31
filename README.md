# AI Coding Agent

## Overview

This project is an AI-powered coding agent built in Python that can understand an existing Node.js codebase and generate an execution plan to implement product requirements with minimal user guidance.

The target repository used is:

https://github.com/callicoder/node-easy-notes-app

---

## Objective

The agent receives a natural language request:

> Improve the application so users can better organise and search their notes.

The agent then:

- Explores the repository
- Identifies important files
- Creates an execution plan using Gemini AI
- Modifies the required files
- Summarizes the performed changes

---

## Project Structure

```
ai-coding-agent/
│
├── agent.py
├── explorer.py
├── planner.py
├── modifier.py
├── llm.py
├── prompts.py
├── README.md
├── .gitignore
└── .env
```

---

## Architecture

```
                User Request
                      │
                      ▼
               AI Coding Agent
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
 Explorer        Planner (Gemini)   Modifier
      │               │               │
      └───────────────┼───────────────┘
                      ▼
              Execution Summary
```

---

## Workflow

### Step 1 – Repository Exploration

The Explorer scans the target repository and identifies important JavaScript and configuration files.

Example:

- server.js
- package.json
- app/models/note.model.js
- app/controllers/note.controller.js
- app/routes/note.routes.js

---

### Step 2 – Planning

The Planner sends the repository information and the user's requirement to Gemini AI.

Gemini generates an execution plan describing:

- Files to modify
- Required changes
- Implementation order

---

### Step 3 – Code Modification

The Modifier:

- Opens the target source file
- Reads the current implementation
- Sends the file content and task to Gemini
- Receives the updated implementation
- Saves the modified source file

---

### Step 4 – Summary

After all modifications, the agent generates a summary listing:

- Modified files
- Implemented features
- Execution status

---

## Technologies Used

- Python 3.11+
- Google Gemini API
- python-dotenv
- pathlib

Target Repository

- Node.js
- Express.js
- MongoDB
- Mongoose

---

## Installation

Clone the repository

```bash
git clone <your_repository_url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Run

```bash
python agent.py
```

---

## Sample Input

```
Improve the application so users can better organise and search their notes.
```

---

## Expected Output

```
Scanning Repository...

Creating Execution Plan...

Executing Plan...

Updated app/models/note.model.js

Updated app/controllers/note.controller.js

Updated app/routes/note.routes.js

Completed Successfully
```

---

## Assumptions

- Repository already exists locally.
- The project is compatible with Node.js.
- Gemini API key is configured.
- Existing functionality should remain unchanged.

---

## Trade-offs

- The implementation focuses on feature addition rather than complete project refactoring.
- AI-generated code may require developer review before production deployment.
- Repository exploration is limited to relevant project files.

---

## Future Improvements

- Multi-file dependency analysis
- Automatic testing after modifications
- Git commit generation
- Rollback support
- Interactive CLI
- Support for multiple programming languages

---

## Author

Sowmiya N

Software Engineer | Full Stack Developer | Python Developer