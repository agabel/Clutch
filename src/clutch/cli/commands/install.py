from .console import console
from pyproject import get_dependencies
from pip._internal.cli.main import main as pipmain
from rich.progress import Progress
import click


@click.command()
def install():
    console.print("Installing...")
    dependencies = get_dependencies()

    with Progress() as progress:
        for dependency in dependencies:
            pipmain(['install', dependency])

    console.print("Done!")
