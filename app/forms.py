from wtforms import Form
from wtforms import StringField, TextField, SelectField, DateField, DateTimeField
from wtforms import validators

class FormLog(Form):
    tipo = SelectField(
        'Tipo:',
        validators= [validators.length(min=5, max = 11, message='Tipo no valido'), validators.input_required(message = 'Entrada requerida.') ],
        choices=[('False', ''),('Information', 'Information'), ('Warning', 'Warning'), ('Error', 'Error')]
        )
    descripcion = StringField(
        'Descripcion:',
        validators= [validators.length(min=5, max = 50, message='La descripcion debe tener al menos 5 caracteres'), validators.input_required(message = 'Entrada requerida.')]
        )
    fecha = DateField(
        'Fecha:',
        validators= [validators.input_required(message = 'Entrada requerida.')]
        )
    hora = StringField(
        'Hora:',
        validators= [validators.input_required(message = 'Entrada requerida.')]
        )
    transaccion = SelectField(
        'Transaccion:',
        validators= [validators.input_required(message = 'Entrada requerida.')],
        choices=[('False', ''),('Transaccion_1', 'Transaccion_1'), ('Transaccion_2', 'Transaccion_2'), ('Transaccion_3', 'Transaccion_3')]
        )
    servicio = SelectField(
        'Servicio:',
        validators= [validators.input_required(message = 'Entrada requerida.')],
        choices=[('False', ''),('Servicio_1', 'Servicio_1'), ('Servicio_2', 'Servicio_2'), ('Servicio_3', 'Servicio_3')]
        )


class FormLogFilter(Form):
    tipo = SelectField(
        'Tipo:',
        validators= [validators.length(min=5, max = 11, message='Tipo no valido'), validators.input_required(message = 'Entrada requerida.')],
        choices=[('False', ''),('Information', 'Information'), ('Warning', 'Warning'), ('Error', 'Error')]
        )
    fecha = DateField(
        'Fecha:',
        validators= [validators.input_required(message = 'Entrada requerida.')]
        )
    hora = StringField(
        'Hora:',
        validators= [validators.input_required(message = 'Entrada requerida.')]
        )
    transaccion = SelectField(
        'Transaccion:',
        validators= [validators.input_required(message = 'Entrada requerida.')],
        choices=[('False', ''),('Transaccion_1', 'Transaccion_1'), ('Transaccion_2', 'Transaccion_2'), ('Transaccion_3', 'Transaccion_3')]
        )
    servicio = SelectField(
        'Servicio:',
        validators= [validators.input_required(message = 'Entrada requerida.')],
        choices=[('False', ''),('Servicio_1', 'Servicio_1'), ('Servicio_2', 'Servicio_2'), ('Servicio_3', 'Servicio_3')]
        )
