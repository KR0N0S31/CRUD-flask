from app.model import Log
from bson.objectid import ObjectId

def __conver_id(collection, _id):
    try:
        return collection.find_one({'_id': ObjectId(_id)})
    except Exception as e:
        return False

def filtrar_logs(collection, filter_tipo, filter_fecha, filter_hora):
    logs_filter = []
    if filter_tipo == 'False':
        filter_tipo = False
    if filter_tipo and filter_fecha and filter_hora:
        cursor = collection.find({"tipo":{"$in":[filter_tipo]},"fecha":{"$in":[filter_fecha]},"hora":{"$in":[filter_hora]}})
    elif filter_tipo and filter_fecha:
        cursor = collection.find({"tipo":{"$in":[filter_tipo]}, "fecha":{"$in":[filter_fecha]}})
    elif filter_tipo and filter_hora:
        cursor = collection.find({"tipo":{"$in":[filter_tipo]},"hora":{"$in":[filter_hora]}})
    elif filter_fecha and filter_hora:
        cursor = collection.find({"fecha":{"$in":[filter_fecha]}, "hora":{"$in":[filter_hora]}})
    elif filter_tipo:
        cursor = collection.find({"tipo":{"$in":[filter_tipo]}})
    elif filter_fecha:
        cursor = collection.find({"fecha":{"$in":[filter_fecha]}})
    elif filter_hora:
        cursor = collection.find({"hora":{"$in":[filter_hora]}})
    else:
        cursor = False
    if cursor:
        for fut in cursor:
            logs_filter.append(Log(fut['tipo'], fut['descripcion'], fut['fecha'], fut['hora'], fut['trasaccion'], fut['servicio'], fut['_id']))
    return logs_filter

def log_for_update(collection, log_id):
    data = __conver_id(collection, log_id)
    if data:
        data_log = Log(data['tipo'], data['descripcion'], data['fecha'], data['hora'], data['trasaccion'], data['servicio'], data['_id'])
        return data_log
    else:
        False

def update(collection,log_id, log):
    log_id = ObjectId(log_id)
    collection.update(
        {"_id":log_id},
        {
            '$set':{
                'tipo':log['tipo'],
                'descripcion':log['descripcion'],
                'fecha':log['fecha'], 'hora':log['hora'],
                'trasaccion':log['trasaccion'],
                'servicio':log['servicio']
            }
        },
        upsert = False,
        multi = False
    )
