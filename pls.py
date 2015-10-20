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
    call(['virtualenv', 'env-' + name])
    venv_file = 'env-' + name + '/bin/activate_this.py'
    execfile(venv_file, dict(__file__=venv_file))
    call(['pip', 'install', 'django'])
    call(['django-admin', 'startproject', name])
    os.chdir(name)
    requirements = open('requirements.txt', 'w+')
    requirements.write('Django\npsycopg2\nwsgiref')
    requirements.close()
    os.mkdir('static')
    os.mkdir('.ebextensions')
    packages = open('.ebextensions/01_packages.config', 'w+')
    packages.write('packages:\n  yum:\n    git: []\n    postgresql93-devel: []\n')
    packages.close()
    py_settings_data = urllib2.urlopen('https://raw.githubusercontent.com/Reparadocs/pls-config/master/02_python.config').read()
    py_settings_data = py_settings_data.replace('REPLACE_THIS', name)
    py_settings = open('.ebextensions/02_python.config', 'w+')
    py_settings.write(py_settings_data)
    py_settings.close()
    gitignore_data = urllib2.urlopen('https://raw.githubusercontent.com/Reparadocs/pls-config/master/.gitignore').read()
    gitignore_data = gitignore_data.replace('REPLACE_THIS', name)
    gitignore = open('.gitignore', 'w+')
    gitignore.write(gitignore_data)
    gitignore.close()
    django_settings_data = urllib2.urlopen('https://raw.githubusercontent.com/Reparadocs/pls-config/master/settings.py').read()
    django_settings_data.replace('REPLACE_THIS', name)
    django_settings = open(name + '/settings.py', 'w')
    django_settings.write(django_settings_data)
    django_settings.close()
    call(['pip', 'install', 'awsebcli'])
    call(['eb', 'init', name, '--region', 'us-west-2', '-p', 'Python2.7', '-i'])
    call(['git', 'add', '--all'])
    call(['git', 'commit', '-m', '"Initial Commit"'])
    call(['eb', 'create', name + '-dev'])
    call(['eb', 'console'])
       
    click.echo('test')

if __name__ == '__main__':
    pls()
