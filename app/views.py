from app import app
from flask import  (Flask,
                    request,
                    redirect,
                    render_template,
                    url_for)

@app.route(r'/', methods =['GET'])
def index():
    return render_template('index.html')
