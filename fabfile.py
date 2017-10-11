from fabric.api import local
from fabric.colors import *

# EG
# def hello(name="world"):
#     print("Hello %s!" % name)

# Fabric help

def help():
    """Display help text"""
    print(blue("\nUsage fab command:arg command:arg etc\n", True))
    print(white("Task list:\n", True))
    print(cyan("fab build", True))
    print(" - Builds the docker image to work with")
    print(cyan("fab run", True))
    print(" - Runs a container, mounting ./code and local /etc/hosts, runs ./code/main.py and removes the container when done")
    print(cyan("fab test", True))
    print(" - Runs a container, mounting ./code and local /etc/hosts, runs ./code/test.py and removes the container when done")


# Build the container
def build():
    local('docker build -t selenium . ')
# Run container and remove after running
def run():
    local('docker run --rm -v $(pwd)/code:/code -v /etc/hosts:/etc/hosts -it selenium python /code/main.py')
# Tests
def test():
    local('docker run --rm -v $(pwd)/code:/code -v /etc/hosts:/etc/hosts -it selenium python /code/test.py')