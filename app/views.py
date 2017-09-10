from flask import request, redirect, render_template, url_for
from app import app
from app.forms import FormLog, FormLogFilter
from app.model import Log
from app.db import *
from app.querys import filtrar_logs, log_for_update, update
from bson.objectid import ObjectId

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
        log = Log(tipo, descripcion, fecha, hora, trasaccion, servicio,0)
        try:
            collection.insert(log.toDBCollection())
        except Exception as e:
            return render_template('create.html', form = log_form, log_create = False, db_not_conn = True)
        log_form = FormLog()
        return render_template('create.html', form = log_form, log_create = True )
    else:
        return render_template('create.html', form = log_form, log_create = False )

@app.route(r'/log', methods =['GET','POST'])
def logs():
    sin_result = 0
    filter_form = FormLogFilter(request.form)
    logs = []
    try:
        cursor = collection.find()
        for fut in cursor:
            logs.append(Log(fut['tipo'], fut['descripcion'], fut['fecha'], fut['hora'], fut['trasaccion'], fut['servicio'],fut['_id']))
    except Exception as e:
        return render_template('read.html', form = filter_form, logs=logs, db_not_conn = True)
    if request.method == 'GET':
        filter_activate = request.args.get('filter_activate', False)
        if filter_activate:
            filter_tipo = request.args.get('tipo', False)
            filter_fecha = request.args.get('fecha', False)
            filter_hora = request.args.get('hora', False)
            try:
                logs_filter = filtrar_logs(collection, filter_tipo ,filter_fecha ,filter_hora)
            except Exception as e:
                 return render_template('read.html', logs=logs_filter, form = filter_form, sin_result = sin_result, db_not_conn = True)
            if len(logs_filter) == 0:
                sin_result = 1
            return render_template('read.html', logs=logs_filter, form = filter_form, sin_result = sin_result, fil = True )
        if len(logs) == 0:
            sin_result = 1
        return render_template('read.html', logs=logs, form = filter_form, sin_result = sin_result )
    else:
        return render_template('read.html', logs=logs, form = filter_form)

@app.route(r'/update', methods =['GET','POST'])
def update_log():
    log_id = request.args.get('log', False)
    data = log_for_update(collection,log_id)
    update_form = FormLog(request.form)
    if request.method == 'POST':
        if update_form.validate():
            tipo = update_form.tipo.data
            if tipo == 'False':
                return render_template('update.html', form = update_form, tipo_not_val = True, data = data )
            descripcion = update_form.descripcion.data
            fecha = str(update_form.fecha.data)
            hora = update_form.hora.data
            trasaccion = update_form.trasaccion.data
            servicio = update_form.servicio.data
            log = Log(tipo, descripcion, fecha, hora, trasaccion, servicio, log_id)
            log = log.toDBCollection()
            try:
                update(collection,log_id,log)
            except Exception as e:
                return render_template('update.html', form = update_form, db_not_conn = True, data = data )
            return redirect(url_for('logs'))
        else:
            return render_template('update.html', form = update_form, db_not_conn = False, data = data )
    elif request.method == 'GET':
        if log_id:
            if data:
                update_form = FormLog(descripcion = data.descripcion, hora = data.hora, trasaccion = data.trasaccion, servicio = data.servicio)
                return render_template('update.html', form = update_form, data = data)
            else:
                return render_template('redirect.html')
        else:
            return render_template('redirect.html')
    else:
        return render_template('redirect.html')

@app.route(r'/delete', methods =['GET','POST'])
def delete_log():
    log_id = request.args.get('log', False)
    if request.method == 'POST' and log_id:
        try:
            log_id= ObjectId(log_id)
            collection.remove({"_id":log_id})
        except Exception as e:
            return render_template('delete.html', db_not_conn = True, data = log_for_update(collection,log_id) )
        return redirect(url_for('logs'))

    elif request.method == 'GET':
        if log_id:
            data = log_for_update(collection,log_id)
            if data:
                return render_template('delete.html', data = data)
            else:
                return render_template('redirect.html')
        else:
            return render_template('redirect.html')
    else:
        return render_template('redirect.html')

# collection.remove({"internacional":True})
