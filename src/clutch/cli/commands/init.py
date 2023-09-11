import sys
import tomlkit
from rich.color import Color
from rich.panel import Panel
import click
from click import command
from pyproject import read_pyproject, pyproject_eixsts
from .console import console


@click.command()
def init():
    Panel.fit("Initializing...", title="Initializing", border_style="green", padding=(1, 2))

    if not pyproject_eixsts():
        pyproject_doc = tomlkit.document()
        project_table = tomlkit.table()
        project_table.add("name", console.input("Project name: "))
        project_table.add("description", console.input("Description: "))
        project_table.add("requires-python", sys.version.split(" ")[0])
        project_table.add("dependencies", [])
        pyproject_doc.add("project", project_table)

        with open('pyproject.toml', 'w') as pyproject_toml:
            pyproject_toml.write(pyproject_doc.as_string())

        console.print(Panel.fit("Created pyproject.toml", title="Success", border_style="green", padding=(1, 2)))

    else:
        console.print(Panel.fit("pyproject.toml already exists", title="Error", border_style="red", padding=(1, 2)))
