# Create a manage.py file and its content is as follows:
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db

# Create an instance of the Manager class   
manager = Manager(app)

# Create an instance of the Migrate class
migrate = Migrate(app, db)

# Add the MigrateCommand to the manager object
manager.add_command('db', MigrateCommand)

# Run the manager
if __name__ == '__main__':
    manager.run()
