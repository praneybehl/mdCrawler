Skip to main content
CLAUDE.md is a project configuration file that Claude Code automatically reads when working in your directory. Claude Code follows CLAUDE.md instructions much more strictly than user prompts, treating them as immutable system rules for your project setup with superior instruction adherence.
### How to Use It​
Create a `CLAUDE.md` file in your project root directory. Claude Code automatically detects and reads this file when starting work in your project. The file uses standard Markdown format and becomes your project's persistent instruction set that Claude follows throughout the entire session.
### Why Use It​
Claude Code has a strict instruction hierarchy where CLAUDE.md content is treated as authoritative system rules, while user prompts are interpreted as flexible requests that must work within those established rules. This hierarchy ensures consistent behavior and higher instruction adherence throughout your Claude Code session.
**Adherence Hierarchy:**
  * **CLAUDE.md instructions** - Treated as immutable system rules that define operational boundaries
  * **User prompts** - Interpreted as flexible requests that must work within established rules
  * **Process execution** - CLAUDE.md steps followed sequentially vs user prompts adapted and optimized


### What to Include​
Include your project's essential information in modular sections: development commands, file boundaries, coding standards, workflow procedures, and any critical processes Claude should follow. Break information into clear markdown modules to prevent instruction bleeding between different functional areas.
**Simple Example:**
```
# CLAUDE.md## Project OverviewPython web API using FastAPI and PostgreSQL.## Commands- python -m venv venv: Create virtual environment- source venv/bin/activate: Activate environment- pip install -r requirements.txt: Install dependencies- uvicorn main:app --reload: Start development server- pytest: Run tests## File Boundaries- Safe to edit: /app/, /tests/, /docs/- Never touch: /venv/, /__pycache__/, /.pytest_cache/## Rules- Use type hints for all functions- Follow PEP 8 style guidelines- Add docstrings to all classes and functions- Write tests for new endpoints## Code Examples```python# Good: Proper typing and documentationfrom typing import List, Optionaldef get_users(limit: int = 10, active_only: bool = True) -> List[User]:  """Retrieve users from database with optional filtering.  Args:    limit: Maximum number of users to return    active_only: Whether to filter for active users only  Returns:    List of User objects  """  return db.query(User).filter(User.is_active == active_only).limit(limit).all()# Bad: Missing types and documentationdef get_users(limit=10, active=True):  return db.query(User).filter(User.is_active == active).limit(limit).all()```
```

### Benefits​
CLAUDE.md provides superior instruction adherence and consistent execution compared to user prompts alone, creating a reliable foundation for complex project workflows.
**Key Benefits:**
  * **Higher Instruction Adherence** - CLAUDE.md content treated as authoritative system rules
  * **Consistent Execution** - Sequential process steps followed systematically throughout session
  * **Context Persistence** - Instructions maintained across entire Claude Code session
  * **Reduced Context Pollution** - Controlled file access prevents unwanted information contamination
  * **Modular Organization** - Clear markdown separations between functional areas prevent instruction bleeding
  * **Token Efficiency** - Front-loaded context reduces guesswork and saves tokens
  * **Workflow Automation** - Persistent processes that don't require re-explanation


I use CLAUDE.md to establish my project's operational boundaries and ensure Claude follows my exact workflows without deviation throughout long coding sessions.
### Advanced Configuration​
**Modular Design** - Break CLAUDE.md into functional modules using clear markdown headers. This prevents instruction bleeding between different areas like development commands, coding standards, and deployment procedures.
**Length Management** - Large CLAUDE.md files provide better instruction adherence despite potential performance warnings. Front-loading complete context is more effective than having Claude read files that may poison the context.
**File Boundaries** - Explicitly define which files Claude can read and which are forbidden. This prevents context contamination from irrelevant or sensitive files.
**Context Control** - Swap out different CLAUDE.md files for different tasks to keep Claude's focus light and task-specific while maintaining the benefits of persistent instructions.
### Getting Started​
Create a `CLAUDE.md` configuration file in your project root with your essential project information, commands, and rules. Start simple and add more detail as needed. For complete setup guidance, see our Installation and Configuration guides.
System Thinking
This approach works best when you thoroughly understand the system you're building. By providing complete context upfront, you minimize Claude's guesswork, leading to better adherence, faster task execution, and token savings.
Avoid Context Poisoning
Keep information that's not pertinent to the current task out of your CLAUDE.md. Extra context can lead to less predictable behavior.
Modular Approach
Use clear markdown sections to separate different functional areas. This prevents instruction bleeding and maintains clear boundaries between different workflow systems.
##### Superior Instruction Adherence
CLAUDE.md content is treated as immutable system rules with strict hierarchical priority over prompts. Modular markdown sections prevent instruction bleeding between different functional workflow areas.
![Custom image](https://www.claudelog.com/img/discovery/026_japan.png)
**See Also** : CLAUDE.md Supremacy | Getting Started | Configuration Guide
  * How to Use It
  * Why Use It
  * What to Include
  * Benefits
  * Advanced Configuration
  * Getting Started


