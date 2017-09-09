from app.model import Log

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
            logs_filter.append(Log(fut['tipo'], fut['descripcion'], fut['fecha'], fut['hora'], fut['trasaccion'], fut['servicio']))
    return logs_filter
