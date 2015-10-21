# pls
#### Django setup made easy.

Pls is a command line utility that creates a new Django project for you and sets it up with AWS Elastic Beanstalk and RDS so that you can start building immediately! Pls spins up micro instances by default so it will fall into the AWS free tier (of course this can be scaled up if you want). Databases are backed by Postgres on AWS and by SQLite locally 

### Installation

##### You'll need:
  - Python 2.7 (`brew install python` or `sudo apt-get install python2.7`)
  - An Amazon AWS Account (http://aws.amazon.com)

I strongly suggest using virtualenv (https://virtualenv.pypa.io/en/latest/) as well, but it is optional
  
##### To Install:

`pip install pls`

### Usage

1. `pls init NAME` (replace NAME with the name of your project)

If prompted, input your AWS Access Keys (https://console.aws.amazon.com/iam/home?region=us-west-2#security_credential)

In 5-10 minutes your project should be 100% ready! It's that easy. A git repository has been initialized for you.

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

Please contact me if you have any problems, questions, comments, etc.! (reparadocs@gmail.com)


Much thanks to RealPython's tutorial: https://realpython.com/blog/python/deploying-a-django-app-to-aws-elastic-beanstalk/ 