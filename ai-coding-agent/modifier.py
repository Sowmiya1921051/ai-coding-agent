class Modifier:

    def __init__(self, project_path):
        self.project_path = project_path

    def execute(self, plan):

        print("\nExecuting Plan...\n")

        for task in plan["tasks"]:
            print(f"File   : {task['file']}")
            print(f"Action : {task['action']}")
            print("-" * 40)

        print("Plan execution completed.")