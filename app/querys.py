from app.model import Log
from bson.objectid import ObjectId

def __conver_id(collection, _id):
    try:
        return collection.find_one({'_id': ObjectId(_id)})
    except Exception as e:
        return False

def filtrar_logs(collection, filter_tipo, filter_fecha, filter_hora, filter_transaccion, filter_servicio):
    logs_filter = []
    if filter_tipo == 'False':
        filter_tipo = False
    if filter_transaccion == 'False':
        filter_transaccion = False
    if filter_servicio == 'False':
        filter_servicio = False
#--------------------------------------/----------------------------------------
    if filter_tipo and filter_fecha and filter_hora and filter_transaccion and filter_servicio:#1-2-3-4-5
        cursor = collection.find({"tipo":{"$in":[filter_tipo]},"fecha":{"$in":[filter_fecha]},"hora":{"$in":[filter_hora]},"transaccion":{"$in":[filter_transaccion]},"servicio":{"$in":[filter_servicio]}})
#--------------------------------------/----------------------------------------
    elif filter_tipo and filter_fecha and filter_hora and filter_transaccion:#1-2-3-4
        cursor = collection.find({"tipo":{"$in":[filter_tipo]},"fecha":{"$in":[filter_fecha]},"hora":{"$in":[filter_hora]},"transaccion":{"$in":[filter_transaccion]}})
    elif filter_tipo and filter_fecha and filter_hora and filter_servicio:#1-2-3-5
        cursor = collection.find({"tipo":{"$in":[filter_tipo]},"fecha":{"$in":[filter_fecha]},"hora":{"$in":[filter_hora]},"servicio":{"$in":[filter_servicio]}})
    elif filter_tipo and filter_hora and filter_transaccion and filter_servicio:#1-3-4-5
        cursor = collection.find({"tipo":{"$in":[filter_tipo]},"hora":{"$in":[filter_hora]},"transaccion":{"$in":[filter_transaccion]},"servicio":{"$in":[filter_servicio]}})
    elif filter_tipo and filter_fecha and filter_transaccion and filter_servicio:#1-2-4-5
        cursor = collection.find({"tipo":{"$in":[filter_tipo]},"fecha":{"$in":[filter_fecha]},"transaccion":{"$in":[filter_transaccion]},"servicio":{"$in":[filter_servicio]}})
    elif filter_fecha and filter_hora and filter_transaccion and filter_servicio:#2-3-4-5
        cursor = collection.find({"fecha":{"$in":[filter_fecha]},"hora":{"$in":[filter_hora]},"transaccion":{"$in":[filter_transaccion]}, "servicio":{"$in":[filter_servicio]}})
#--------------------------------------/----------------------------------------
    elif filter_tipo and filter_fecha and filter_hora:#1-2-3
        cursor = collection.find({"tipo":{"$in":[filter_tipo]},"fecha":{"$in":[filter_fecha]},"hora":{"$in":[filter_hora]}})
    elif filter_tipo and filter_fecha and filter_transaccion:#1-2-4
        cursor = collection.find({"tipo":{"$in":[filter_tipo]},"fecha":{"$in":[filter_fecha]},"transaccion":{"$in":[filter_transaccion]}})
    elif filter_tipo and filter_fecha and filter_servicio:#1-2-5
        cursor = collection.find({"tipo":{"$in":[filter_tipo]},"fecha":{"$in":[filter_fecha]},"servicio":{"$in":[filter_servicio]}})
    elif filter_tipo and filter_hora and filter_transaccion:#1-3-4
        cursor = collection.find({"tipo":{"$in":[filter_tipo]},"hora":{"$in":[filter_hora]},"transaccion":{"$in":[filter_transaccion]}})
    elif filter_tipo and filter_hora and filter_servicio:#1-3-5
        cursor = collection.find({"tipo":{"$in":[filter_tipo]},"hora":{"$in":[filter_hora]},"servicio":{"$in":[filter_servicio]}})
    elif filter_tipo and filter_transaccion and filter_servicio:#1-4-5
        cursor = collection.find({"tipo":{"$in":[filter_tipo]},"transaccion":{"$in":[filter_transaccion]},"servicio":{"$in":[filter_servicio]}})
    elif filter_fecha and filter_hora and filter_transaccion:#2-3-4
        cursor = collection.find({"fecha":{"$in":[filter_fecha]},"hora":{"$in":[filter_hora]},"transaccion":{"$in":[filter_transaccion]}})
    elif filter_fecha and filter_hora and filter_servicio:#2-3-5
        cursor = collection.find({"fecha":{"$in":[filter_fecha]},"hora":{"$in":[filter_hora]},"servicio":{"$in":[filter_servicio]}})
    elif filter_fecha and filter_transaccion and filter_servicio:#2-4-5
        cursor = collection.find({"fecha":{"$in":[filter_fecha]},"transaccion":{"$in":[filter_transaccion]},"servicio":{"$in":[filter_servicio]}})
    elif filter_hora and filter_transaccion and filter_servicio:#3-4-5
        cursor = collection.find({"hora":{"$in":[filter_hora]},"transaccion":{"$in":[filter_transaccion]},"servicio":{"$in":[filter_servicio]}})
#--------------------------------------/----------------------------------------
    elif filter_tipo and filter_fecha:#1-2
        cursor = collection.find({"tipo":{"$in":[filter_tipo]}, "fecha":{"$in":[filter_fecha]}})
    elif filter_tipo and filter_hora:#1-3
        cursor = collection.find({"tipo":{"$in":[filter_tipo]},"hora":{"$in":[filter_hora]}})
    elif filter_tipo and filter_transaccion:
        cursor = collection.find({"tipo":{"$in":[filter_tipo]},"transaccion":{"$in":[filter_transaccion]}})
    elif filter_tipo and filter_servicio:#1-4
        cursor = collection.find({"tipo":{"$in":[filter_tipo]},"servicio":{"$in":[filter_servicio]}})
    elif filter_fecha and filter_hora:#2-3
        cursor = collection.find({"fecha":{"$in":[filter_fecha]}, "hora":{"$in":[filter_hora]}})
    elif filter_fecha and filter_transaccion:#2-4
        cursor = collection.find({"fecha":{"$in":[filter_fecha]}, "transaccion":{"$in":[filter_transaccion]}})
    elif filter_fecha and filter_servicio:#2-5
        cursor = collection.find({"fecha":{"$in":[filter_fecha]}, "servicio":{"$in":[filter_servicio]}})
    elif filter_hora and filter_transaccion:#3-4
        cursor = collection.find({"hora":{"$in":[filter_hora]}, "transaccion":{"$in":[filter_transaccion]}})
    elif filter_hora and filter_servicio:#3-5
        cursor = collection.find({"hora":{"$in":[filter_hora]}, "servicio":{"$in":[filter_servicio]}})
    elif filter_transaccion and filter_servicio:#4-5
        cursor = collection.find({"transaccion":{"$in":[filter_transaccion]}, "servicio":{"$in":[filter_servicio]}})
#--------------------------------------/----------------------------------------
    elif filter_tipo:#1
        cursor = collection.find({"tipo":{"$in":[filter_tipo]}})
    elif filter_fecha:#2
        cursor = collection.find({"fecha":{"$in":[filter_fecha]}})
    elif filter_hora:#3
        cursor = collection.find({"hora":{"$in":[filter_hora]}})
    elif filter_transaccion:#4
        cursor = collection.find({"transaccion":{"$in":[filter_transaccion]}})
    elif filter_servicio:#5
        cursor = collection.find({"servicio":{"$in":[filter_servicio]}})
#--------------------------------------/----------------------------------------
    else:
        cursor = False
    if cursor:
        for fut in cursor:
            logs_filter.append(Log(fut['tipo'], fut['descripcion'], fut['fecha'], fut['hora'], fut['transaccion'], fut['servicio'], fut['_id']))
    return logs_filter

def log_for_update(collection, log_id):
    data = __conver_id(collection, log_id)
    if data:
        data_log = Log(data['tipo'], data['descripcion'], data['fecha'], data['hora'], data['transaccion'], data['servicio'], data['_id'])
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
                'transaccion':log['transaccion'],
                'servicio':log['servicio']
            }
        },
        upsert = False,
        multi = False
    )
