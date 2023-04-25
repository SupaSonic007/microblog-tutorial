from app import mail
from flask_mail import Message

msg = Message('test subject', sender=app.config['ADMINS'][0], recipients=['joshuakonline@gmail.com'])

msg.body = 'text body'

msg.html = '<h1>HTML body</h1>'

mail.send(msg)