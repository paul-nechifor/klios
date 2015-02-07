import os
from fabric.api import local, task, prefix, lcd

root = os.path.dirname(os.path.realpath(__file__)) + '/..'


@task
def bootstrap():
    local('virtualenv env')
    with prefix('. env/bin/activate'):
        local('pip install -r requirements/base.txt')
        local('site/manage.py migrate')


@task
def runserver():
    with lcd(root):
        local('. env/bin/activate && site/manage.py runserver')
