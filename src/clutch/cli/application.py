import os
import sys
import time

import click
from .commands.add import add
from .commands.init import init
from .commands.install import install
from .commands.lock import lock
from .commands.vendorize import vendorize


@click.group()
def cli():
    pass


cli.add_command(init)
cli.add_command(add)
cli.add_command(install)
cli.add_command(lock)
cli.add_command(vendorize)


