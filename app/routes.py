from flask import Flask, render_template, request, flash
from app.forms import ContactForm
from flask_mail import Mail, Message


app = Flask(__name__)

# Prevents Cross-Site Request Forgery Attacks
app.secret_key = 'dev key'
app.config.update(
	DEBUG=True,
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'maciejsmusz@gmail.com',
	MAIL_PASSWORD = ''
	)
mail = Mail(app)
# https://myaccount.google.com/lesssecureapps?rfn=27&rfnc=1&eid=-2603848626940582045&et=0&asae=2&pli=1

@app.route('/')
def home():
    return render_template('home.html'), 200

@app.route('/about')
def about():
    return render_template('about.html', ), 200

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm(request.form)
    if request.method == 'POST':
        if not form.email.data:
            return render_template('contact.html', form=form)
        else:
            try:
                msg = Message(form.subject.data, sender='maciejsmusz@gmail.com', recipients=['msmusz@student.neumont.edu', 'wesleysheng@gmail.com'])
                msg.body = """From %s <%s> \n%s""" % (form.name.data, form.email.data, form.message.data)
                mail.send(msg)
                return 'Form Posted'
            except Exception as e:
                return (str(e))


    elif request.method == 'GET':
        return render_template('contact.html', form=form)
app.run(debug=True)