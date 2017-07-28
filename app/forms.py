from wtforms import Form, StringField, TextAreaField, SubmitField, validators, ValidationError
from wtforms.fields.html5 import EmailField

class ContactForm(Form):
    name = StringField("Name")
    email = EmailField("Email")
    subject = StringField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")
