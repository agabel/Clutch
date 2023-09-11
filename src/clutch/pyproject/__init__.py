import tomlkit
import io
import os


def pyproject_eixsts() -> bool:
    return os.path.exists('pyproject.toml')


def read_pyproject():
    with io.open('pyproject.toml') as pyproject_toml:
        toml = tomlkit.load(pyproject_toml)
        return toml


def add_dependency(dependency):
    with io.open('pyproject.toml', 'r') as pyproject_toml:
        toml = tomlkit.load(pyproject_toml)
        toml['project']['dependencies'].append(dependency)
        
    with io.open('pyproject.toml', 'w') as pyproject_toml:
        pyproject_toml.write(tomlkit.dumps(toml))


def get_dependencies():
    with io.open('pyproject.toml', 'r') as pyproject_toml:
        toml = tomlkit.load(pyproject_toml)
        return toml['project']['dependencies']
