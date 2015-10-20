# pls
#### Django setup made easy.

Pls is a command line utility that creates a new Django project for you and sets it up with AWS Elastic Beanstalk and RDS so that you can start building immediately! Pls spins up micro instances by default so it will fall into the AWS free tier (of course this can be scaled up if you want)

### Installation

##### You'll need:
  - Python 2.7 (`brew install python` or `sudo apt-get install python2.7`)
  - PIP 
  - VirtualEnv (`pip install virtualenv`)
  - Postgres (`brew install postgres` or `sudo apt-get install postgresql`)
  - An Amazon AWS Account (http://aws.amazon.com)
  
##### To Install:

`pip install pls`

### Usage

1. Create and `cd` into a new directory for your project
2. `pls init NAME` (replace NAME with the name of your project)
3. When prompted, input your AWS Access Keys (https://console.aws.amazon.com/iam/home?region=us-west-2#security_credential)

In 5-10 minutes your project should be 100% ready, run `source venv/bin/activate` to activate the VirtualEnv and start coding!

A git repository has been initialized for you.

##### To deploy to AWS:

1. Commit to git
2. `eb deploy`

##### Other useful commands:

`eb logs` - To view AWS logs

`eb open` - Open your website

`eb console` - Open the AWS console



### Planned Features:

- S3 Integration
- GitHub Integration
