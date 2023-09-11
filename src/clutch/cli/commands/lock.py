import sys
import tomlkit
from rich.color import Color
from rich.panel import Panel
import click
from click import command
from pyproject import get_dependencies
from .console import console


@click.command()
def lock():
    dependencies = get_dependencies()

    with open('clutch.lock', 'w') as lockfile:
        for dependency in dependencies:
            lockfile.write(dependency + '\n')
