import toml
import pathlib

class Project():
    def __init__(self, name: str, license: str, description: str, authors: [], dependencies: dict, devdependencies: dict):
        self.name = name
        self.license = license
        self.description = description
        self.authors = authors
        self.dependencies = list(dependencies.keys())
        self.devdependencies = list(devdependencies.keys())

        if not self.name:
            self.name = "N/A"
        
        if not self.license:
            self.license = "N/A"

        if not self.description:
            self.description = "N/A"
        
        if not self.authors:
            self.authors = "N/A"

        if not self.dependencies:
            self.dependencies = "N/A"

        if not self.devdependencies:
            self.devdependencies = "N/A"
    
    def __str__(self):
        authors_str = "\n- ".join(self.authors) if isinstance(self.authors, list) else self.authors
        dependencies_str = "\n- ".join(self.dependencies) if isinstance(self.dependencies, list) else self.dependencies
        devdependencies_str = "\n- ".join(self.devdependencies) if isinstance(self.devdependencies, list) else self.devdependencies

        return f"Name: {self.name}\nDescription: {self.description}\nLicense: {self.license}\n\nAuthors: \n- {authors_str}\n\nDependencies: \n- {dependencies_str}\n\nDevelopment Dependencies: \n- {devdependencies_str}"

class ProjectReader():
    def __init__(self):
        self._url = str(pathlib.Path(__file__).parent.resolve())
        self._url = self._url[:-3]
        self._url = self._url + "/pyproject.toml"

    def get_project(self):
        with open(self._url) as f:
            content = f.read()

        parsed_toml = toml.loads(content)

        try:
            project_name = parsed_toml["tool"]["poetry"]["name"]
        except:
            project_name = ""

        try:
            project_license = parsed_toml["tool"]["poetry"]["license"]
        except:
            project_license = ""
        
        try:
            project_description = parsed_toml["tool"]["poetry"]["description"]
        except:
            project_description = ""
        
        try:
            project_authors = parsed_toml["tool"]["poetry"]["authors"]
        except:
            project_authors = []

        try:
            project_dependencies = parsed_toml["tool"]["poetry"]["dependencies"]
        except:
            project_dependencies = {}

        try:
            project_devdependencies = parsed_toml["tool"]["poetry"]["group"]["devdependencies"]["dependencies"]
        except:
            project_devdependencies = {}

        return Project(project_name, project_license, project_description, project_authors, project_dependencies, project_devdependencies)
