from app import app

PORT = 80
DEBUG = True

if __name__ == '__main__':
    app.run(port = PORT, debug = DEBUG)
