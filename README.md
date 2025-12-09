# Build Your First ADK Agent Workforce

This project demonstrates how to build and deploy your first agent workforce using the Google Agent Development Kit (ADK).

## Prerequisites

*   Python 3.7+
*   An internet connection

## Setup

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository-url>
    cd my-adk-workforce
    ```
    *(If you are following along by creating files manually, skip this step and create the `my-adk-workforce` directory and its contents as described in the tutorial.)*

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install google-generativeai
    ```

## Running the Application

Execute the main script from your project's root directory:

```bash
python src/main.py
```

This will instantiate the agents, create a workforce, dispatch tasks, and print the results to the console.

## Project Structure

```
my-adk-workforce/
├── venv/
├── src/
│   ├── agent.py
│   └── main.py
└── README.md
```

*   `src/agent.py`: Contains the definition of our custom agent.
*   `src/main.py`: The main entry point for the application, setting up the workforce and tasks.
*   `README.md`: This file.
