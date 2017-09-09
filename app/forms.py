from wtforms import Form
from wtforms import StringField, TextField, SelectField, DateField, DateTimeField
from wtforms import validators

class FormLog(Form):
    tipo = SelectField(
        'Tipo:',
        validators= [validators.length(min=5, max = 11, message='Tipo no valido'), validators.input_required(message = 'Entrada requerida.') ],#,tipo_valido],
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
    trasaccion = TextField(
        'Trasaccion:',
        validators= [validators.input_required(message = 'Entrada requerida.')]
        )
    servicio = TextField(
        'Servicio:',
        validators= [validators.input_required(message = 'Entrada requerida.')]
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
