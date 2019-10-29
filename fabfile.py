from invoke import task

# EG
# def hello(name="world"):
#     print("Hello %s!" % name)

@task
def test(c):
    """Runs a container, mounting ./code and local /etc/hosts, runs ./code/test.py and removes the container when done"""
    c.run('docker run --rm -v $(pwd)/code:/code -v /etc/hosts:/etc/hosts missing_people python3 /code/test.py')

@task
def build(c):
    """Builds the docker image to work with"""
    c.run('docker build missing_people .')

@task
def run(c):
    """Runs a container, mounting ./code and local /etc/hosts, runs ./code/main.py and removes the container when done"""
    c.run('docker run --rm -v $(pwd)/code:/code -v /etc/hosts:/etc/hosts missing_people python3 /code/main.py')
