from cleo import Application
from commands import AddCommand, RemoveCommand, InitCommand, InstallCommand, UpdateCommand, RunCommand


application = Application()
application.add(InitCommand())
application.add(InstallCommand())
application.add(AddCommand())
application.add(RemoveCommand())
application.add(UpdateCommand())
application.add(RunCommand())


if __name__ == "__main__":
    application.run()
