import rich
from rich.progress import Progress
from rich.spinner import Spinner
from rich import console
from rich.color import Color
from rich.panel import Panel
import click
from .console import console
from time import sleep
from pip._internal.cli.main import main as pipmain
from pyproject import add_dependency



@click.command()
@click.argument('package')
def add(package):
    from rich.table import Column
    from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn, SpinnerColumn

    spinner_column = SpinnerColumn()
    text_column = TextColumn(f"Installing {package}...", table_column=Column(ratio=1))
    bar_column = BarColumn(bar_width=None, table_column=Column(ratio=2))
    time_elapsed = TimeElapsedColumn()
    progress = Progress(spinner_column, text_column, bar_column, time_elapsed, expand=True)
    task_1 = progress.add_task(add_dependency(package), total=1)

    while not progress.finished:
        progress.update(task_1, advance=1)


