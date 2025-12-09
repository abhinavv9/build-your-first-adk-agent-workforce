from google_generativeai.agency import Agent, Task, Workforce
from src.agent import MyFirstAgent

def main():
    # Create agents
    agent1 = MyFirstAgent(name="Agent-Alpha")
    agent2 = MyFirstAgent(name="Agent-Beta")

    # Create a workforce with the agents
    workforce = Workforce(agents=[agent1, agent2])

    # Define tasks
    tasks = [
        Task(input="Process Item A"),
        Task(input="Process Item B"),
        Task(input="Process Item C")
    ]

    # Assign tasks to the workforce
    results = workforce.dispatch_tasks(tasks)

    # Print results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()