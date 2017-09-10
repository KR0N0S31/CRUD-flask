from app import app
from flask.ext.script import Manager, Server
from flask_wtf import CsrfProtect

__author__ = 'Felipe Martinez'

csrf=CsrfProtect(app)
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
