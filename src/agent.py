from google_generativeai.agency import Agent, Task

class MyFirstAgent(Agent):
    def __init__(self, name: str):
        super().__init__(name)

    def run(self, task: Task) -> str:
        return f"Agent {self.name} processed task: {task.input}"