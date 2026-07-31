from explorer import Explorer
from planner import Planner
from modifier import Modifier

print("=" * 60)
print("AI Coding Agent")
print("=" * 60)

project_path = "../node-easy-notes-app-master"

# Ask the user for the requirement
request = input("\nEnter your request:\n> ")

explorer = Explorer(project_path)
repository = explorer.scan()

planner = Planner()
plan = planner.create_plan(request, repository)

modifier = Modifier(project_path)
modifier.execute(plan)

print("\nCompleted Successfully")