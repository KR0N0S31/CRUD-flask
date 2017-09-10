from flask import request, redirect, render_template, url_for
from app import app
from app.forms import FormLog, FormLogFilter
from app.model import Log
from app.db import *
from app.filters import filtrar_logs

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@app.route('/', methods =['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/create', methods =['GET','POST'])
def create():
    log_form = FormLog(request.form)
    if request.method == 'POST' and log_form.validate():
        tipo = log_form.tipo.data
        if tipo == 'False':
            return render_template('create.html', form = log_form, log_create = False, tipo_not_val = True)
        descripcion = log_form.descripcion.data
        fecha = str(log_form.fecha.data)
        hora = log_form.hora.data
        trasaccion = log_form.trasaccion.data
        servicio = log_form.servicio.data

        log = Log(tipo, descripcion, fecha, hora, trasaccion, servicio)
        collection.insert(log.toDBCollection())

        log_form = FormLog()
        return render_template('create.html', form = log_form, log_create = True )
    else:
        return render_template('create.html', form = log_form, log_create = False )


@app.route(r'/read', methods =['GET','POST'])
def read():
    sin_result = 0
    filter_form = FormLogFilter(request.form)
    logs = []
    cursor = collection.find()
    for fut in cursor:
        logs.append(Log(fut['tipo'], fut['descripcion'], fut['fecha'], fut['hora'], fut['trasaccion'], fut['servicio']))
    if request.method == 'GET':
        filter_activate = request.args.get('filter_activate', False)
        if filter_activate:
            filter_tipo = request.args.get('tipo', False)
            filter_fecha = request.args.get('fecha', False)
            filter_hora = request.args.get('hora', False)
            logs_filter = filtrar_logs(collection, filter_tipo ,filter_fecha ,filter_hora)
            if len(logs_filter) == 0:
                sin_result = 1
            return render_template('read.html', logs=logs_filter, form = filter_form, sin_result = sin_result, fil = True )
        return render_template('read.html', logs=logs, form = filter_form, sin_result = sin_result )
    else:
        return render_template('read.html', logs=logs)


@app.route(r'/update', methods =['GET','POST'])
def update():
    return render_template('update.html', logs=logs)
