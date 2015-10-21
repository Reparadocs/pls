import click
import os
import pip
import urllib2
from subprocess import call

@click.group()
def pls():
	pass

@pls.command()
@click.argument('name')
def init(name):
    first_app = raw_input('Name your Django app (different from project name): ')
    call(['django-admin', 'startproject', name])
    os.chdir(name)
    call(['git', 'init'])
    requirements_data = urllib2.urlopen('https://raw.githubusercontent.com/Reparadocs/pls-config/master/requirements.txt').read()
    requirements = open('requirements.txt', 'w+')
    requirements.write(requirements_data)
    requirements.close()
    os.mkdir('static')
    gitkeep = open('static/.gitkeep', 'w+')
    gitkeep.close()
    os.mkdir('.ebextensions')
    packages = open('.ebextensions/01_packages.config', 'w+')
    packages.write('packages:\n  yum:\n    git: []\n    postgresql93-devel: []\n')
    packages.close()
    py_settings_data = urllib2.urlopen('https://raw.githubusercontent.com/Reparadocs/pls-config/master/02_python.config').read()
    py_settings_data = py_settings_data.replace('REPLACE_THIS', name)
    py_settings = open('.ebextensions/02_python.config', 'w+')
    py_settings.write(py_settings_data)
    py_settings.close()
    call(['python', 'manage.py', 'startapp', first_app])
    django_settings_data = urllib2.urlopen('https://raw.githubusercontent.com/Reparadocs/pls-config/master/settings.py').read()
    django_settings_data = django_settings_data.replace('REPLACE_THIS', name)
    django_settings_data = django_settings_data.replace('RTHIS_APP', first_app)
    django_settings = open(name + '/settings.py', 'w')
    django_settings.write(django_settings_data)
    django_settings.close()
    call(['python', 'manage.py', 'migrate'])
    gitignore_data = urllib2.urlopen('https://raw.githubusercontent.com/Reparadocs/pls-config/master/.gitignore').read()
    gitignore_data = gitignore_data.replace('REPLACE_THIS', name)
    gitignore = open('.gitignore', 'w+')
    gitignore.write(gitignore_data)
    gitignore.close()
    call(['eb', 'init', name, '--region', 'us-west-2', '-p', 'Python2.7', '-i'])
    call(['git', 'add', '--all'])
    call(['git', 'commit', '-m', '"Initial Commit"'])
    call(['eb', 'create', name + '-dev', '--database.engine', 'postgres', '--timeout', '99999999'])
    call(['eb', 'console'])

def main():
    pls()
       
if __name__ == '__main__':
    main()
