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
    call(['git', 'init'])
    call(['virtualenv', 'venv'])
    venv_file = 'venv/bin/activate_this.py'
    execfile(venv_file, dict(__file__=venv_file))
    call(['pip', 'install', 'django'])
    call(['pip', 'install', 'psycopg2'])
    requirements_data = urllib2.urlopen('https://raw.githubusercontent.com/Reparadocs/pls-config/master/requirements.txt').read()
    requirements = open('requirements.txt', 'w+')
    requirements.write(requirements_data)
    requirements.close()
    call(['django-admin', 'startproject', name])
    os.chdir(name)
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
    django_settings_data = urllib2.urlopen('https://raw.githubusercontent.com/Reparadocs/pls-config/master/settings.py').read()
    django_settings_data = django_settings_data.replace('REPLACE_THIS', name)
    django_settings = open(name + '/settings.py', 'w')
    django_settings.write(django_settings_data)
    django_settings.close()
    os.chdir('..')
    gitignore_data = urllib2.urlopen('https://raw.githubusercontent.com/Reparadocs/pls-config/master/.gitignore').read()
    gitignore_data = gitignore_data.replace('REPLACE_THIS', name)
    gitignore = open('.gitignore', 'w+')
    gitignore.write(gitignore_data)
    gitignore.close()
    call(['pip', 'install', 'awsebcli'])
    call(['eb', 'init', name, '--region', 'us-west-2', '-p', 'Python2.7', '-i'])
    call(['git', 'add', '--all'])
    call(['git', 'commit', '-m', '"Initial Commit"'])
    call(['eb', 'create', name + '-dev', '--database.engine', 'postgres'])
    call(['eb', 'console'])

def main():
    pls()
       
if __name__ == '__main__':
    main()
