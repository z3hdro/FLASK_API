import os
from config import Config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import pytest
from app import app, db

app.config.from_object(Config)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
    pytest.main(["-s", "tests"])

if __name__ == '__main__':
    manager.run()
