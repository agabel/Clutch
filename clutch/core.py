import json
from os import read
import subprocess
from pip._internal.cli.main import main as pipmain


def add(package):
    clutch_data = read_clutchfile()
    if 'packages' not in clutch_data.keys():
        clutch_data['packages'] = {
            "default": [],
            "dev": [],
            "test": []
        }
    clutch_data['packages']['default'].append(package)
    update_clutchfile(clutch_data)


def remove(package):
    pipmain(['uninstall', package])


def install():
    clutch_data = read_clutchfile()
    for package in clutch_data['packages']['default']:
        pipmain(['install', package])
        

def get_default_python_version():
    python_version_result = subprocess.run(['python', '--version'], stdout=subprocess.PIPE)
    python_version_string = python_version_result.stdout.decode('utf-8').replace("Python ", "").replace("\n", "")
    python_version = ".".join(python_version_string.split(".")[0:2])
    return python_version


def generate_clutchfile():
    clutch = {
        "packages": {
            "default": [],
            "dev": [],
            "tests": [],
        },
        "python_version": get_default_python_version()
    }

    pretty_clutch = json.dumps(clutch, indent=4, sort_keys=True)

    with open("./Clutchfile", 'w') as cf:
        cf.writelines(pretty_clutch)
        cf.write('\n')
        

def generate_lockfile():
    lock = {

    }
    
    pretty_lock = json.dumps(lock, indent=4, sort_keys=True)

    with open("./Clutchfile.lock", 'w') as cf:
        cf.writelines(pretty_lock)
        cf.write('\n')


def read_clutchfile():
    with open("./Clutchfile", "r") as cf:
        json_data = json.load(cf)
        return json_data
    return None

def update_clutchfile(cf_data):
    with open("./Clutchfile", "w") as cf:
        cf.writelines(json.dumps(cf_data, indent=4, sort_keys=True))
        cf.write("\n")
        cf.close()
