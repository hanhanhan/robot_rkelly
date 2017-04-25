#!/usr/bin/python

import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db

# set environment variables
# hard code file name?
if os.path.exists('rkelly.env'):
    print('Importing environment from rkelly.env')
    with open('rkelly.env') as env_variables:
        for line in env_variables:
            var = line.strip().split('=')
            if len(var) is 2:
                os.environ[var[0]] = var[1]
else:
    print('not importing env')

application = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(application)
migrate = Migrate(application, db)


def make_shell_context():
    return dict(app=application)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()


