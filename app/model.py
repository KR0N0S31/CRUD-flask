
class Log:
    def __init__(self, tipo, descripcion, fecha, hora, trasaccion, servicio):
        self.tipo = tipo
        self.descripcion = descripcion
        self.fecha = fecha
        self.hora = hora
        self.trasaccion = trasaccion
        self.servicio = servicio

    def toDBCollection (self):
        return {
            "tipo":self.tipo,
            "descripcion":self.descripcion,
            "fecha": self.fecha,
            "hora": self.hora,
            "trasaccion":self.trasaccion,
            "servicio":self.servicio
        }

    def __str__(self):
        return "Tipo: {} - Descripcion: {} - Fecha: {} - Hora: {} - Trasaccion: {} - Servicio: {}".format(self.tipo, self.descripcion, self.fecha, self.hora, self.trasaccion, self.servicio)

# Tipo
# Descripción.
# Fecha hora,
# Trasaccion, 
# Servicio 
