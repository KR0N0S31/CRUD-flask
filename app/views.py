from flask import request, redirect, render_template, url_for
from app import app
from app.forms import FormLog
from app.model import Log
from app.db import *

@app.route('/', methods =['GET'])
def index():
    return render_template('index.html')

@app.route('/create', methods =['GET','POST'])
def create():
    log_form = FormLog(request.form)
    if request.method == 'POST' and log_form.validate():
        tipo = log_form.tipo.data
        descripcion = log_form.descripcion.data
        fecha = str(log_form.fecha.data)
        hora = log_form.hora.data
        print(fecha)
        trasaccion = log_form.trasaccion.data
        servicio = log_form.servicio.data
        log = Log(tipo, descripcion, fecha, hora, trasaccion, servicio)

        collection.insert(log.toDBCollection())

        log_form = FormLog()
        return render_template('create.html', form = log_form, log_create = True )
    else:
        return render_template('create.html', form = log_form, log_create = False )

@app.route(r'/read', methods =['GET'])
def read():
    if request.method == 'GET':
        search = request.args.get('search', '')
        return render_template('read.html')
    else:
        return render_template('read.html')
