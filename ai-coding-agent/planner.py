import json


class Planner:

    def create_plan(self, request, repo):

        print("\nCreating Execution Plan...\n")

        plan = {
            "tasks": [
                {
                    "file": "app/models/note.model.js",
                    "action": "Add category field"
                },
                {
                    "file": "app/models/note.model.js",
                    "action": "Add tags field"
                },
                {
                    "file": "app/controllers/note.controller.js",
                    "action": "Implement search API"
                },
                {
                    "file": "app/routes/note.routes.js",
                    "action": "Add search route"
                }
            ]
        }

        print(json.dumps(plan, indent=4))

        return plan