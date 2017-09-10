
class Log:
    def __init__(self, tipo, descripcion, fecha, hora, transaccion, servicio, log_id):
        self.log_id = log_id
        self.tipo = tipo
        self.descripcion = descripcion
        self.fecha = fecha
        self.hora = hora
        self.transaccion = transaccion
        self.servicio = servicio

    def toDBCollection (self):
        return {
            "tipo":self.tipo,
            "descripcion":self.descripcion,
            "fecha": self.fecha,
            "hora": self.hora,
            "transaccion":self.transaccion,
            "servicio":self.servicio
        }

    def __str__(self):
        return "Tipo: {} - Descripcion: {} - Fecha: {} - Hora: {} - Transaccion: {} - Servicio: {}".format(self.tipo, self.descripcion, self.fecha, self.hora, self.transaccion, self.servicio)
