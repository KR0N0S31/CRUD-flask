from wtforms import Form
from wtforms import StringField, TextField, SelectField, DateField, DateTimeField
from wtforms import validators

class FormLog(Form):
    tipo = SelectField(
        'tipo',
        validators= [validators.length(min=5, max = 11, message='Tipo no valido'), validators.input_required(message = 'Entrada requerida.')],
        choices=[('Information', 'Information'), ('Warning', 'Warning'), ('Error', 'Error')]
        )
    descripcion = StringField(
        'descripcion',
        validators= [validators.length(min=5, max = 50, message='Descripcion no valida'), validators.input_required(message = 'Entrada requerida.')]
        )
    fecha = DateField(
        'fecha',
        validators= [validators.input_required(message = 'Entrada requerida.')]
        )
    hora = StringField(
        'hora',
        validators= [validators.input_required(message = 'Entrada requerida.')]
        )
    trasaccion = TextField(
        'trasaccion',
        validators= [validators.input_required(message = 'Entrada requerida.')]
        )
    servicio = TextField(
        'servicio',
        validators= [validators.input_required(message = 'Entrada requerida.')]
        )
