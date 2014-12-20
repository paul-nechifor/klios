import os
from fabric.api import *

@task
def bootstrap():
    local('virtualenv env')
    with prefix('. env/bin/activate'):
        local('pip install -r requirements/base.txt')
        local('site/manage.py migrate')

@task
def runserver():
    local('. env/bin/activate && site/manage.py runserver')
