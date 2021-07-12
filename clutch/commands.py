from cleo import Command
from core import add, remove, install, generate_clutchfile, generate_lockfile


class AddCommand(Command):
    """
    Install package

    add
        {package : What package do you want to install?}
    """

    def handle(self):
        package = self.argument('package')

        self.line("Installing package: {0}".format(package))

        add(package)

        self.line("Package installed")


class RemoveCommand(Command):
    """
    Remove package

    remove
        {package : What package do you want to install?}
    """

    def handle(self):
        package = self.argument('package')

        self.line("Installing package: {0}".format(package))

        remove(package)

        self.line("Package installed")


class InitCommand(Command):
    """
    Initialize project and create dependency list
    
    init
    """

    def handle(self):
        self.line("Initializing project dependencies")
        generate_clutchfile()
        generate_lockfile()


class InstallCommand(Command):
    """
    Initialize project and create dependency list
    
    install
    """

    def handle(self):
        self.line("Installing dependencies")
        install()


class UpdateCommand(Command):
    """
    Update all dependencies to their latest versions

    update
    """
    
    def handle(self):
        self.line("Updating dependencies")
        

class RunCommand(Command):
    """
    Run scripts
    
    run
    """

    def handle(self):
        self.line("Running command")
