def create_modifier_prompt(file_path, code, action):
    return f"""
You are a senior Node.js engineer.

Task:
{action}

File:
{file_path}

Current Code:
```javascript
{code}