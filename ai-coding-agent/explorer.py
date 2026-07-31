from pathlib import Path


class Explorer:

    def __init__(self, project_path):
        self.project_path = Path(project_path)

        self.ignore_dirs = {
            "node_modules",
            ".git",
            "__pycache__",
            ".vscode",
            ".idea"
        }

    def scan(self):

        print("\nScanning Repository...\n")

        important = []

        for file in self.project_path.rglob("*"):

            # Skip ignored folders
            if any(part in self.ignore_dirs for part in file.parts):
                continue

            if file.is_file():

                if file.suffix in [".js", ".json"]:

                    relative = file.relative_to(self.project_path)

                    important.append(str(relative))

        print("Important Files\n")

        for f in important:
            print(f)

        return {
            "important": important
        }