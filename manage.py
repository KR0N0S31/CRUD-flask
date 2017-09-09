from app import app
from flask.ext.script import Manager, Server

__author__ = 'Felipe Martinez'

manager = Manager(app)

manager.add_command('runserver', Server(
    use_debugger = True,
    use_reloader = True,
    host = 'localhost'
    )
)

# PORT = 8000

if __name__ == '__main__':
    manager.run()
