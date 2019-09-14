from app.resources.Common.Base import Base
from flask_mail import Mail, Message
from flask import session, current_app, redirect,request
import os


class Email(Base):
    @staticmethod
    def send_email_votes(email, login, id, doc):
        mail = Mail(current_app)
        host = os.environ['HOST']
        link = "http://{}:4440/api/email?login={}&id={}&doc={}".format(host, login, id, doc)
        html = """  <h3>Добрый день {}!<h3>
                    <p>Открылось новое голосвание, пройдите, пожалайста, по ссылке</p>
                    <a href={}>Перейти</a>
                """.format(login, link)
        msg = Message(
            subject="Хакатон Голосвание SegFault",
            sender=current_app.config.get("MAIL_USERNAME"),
            recipients=[email],
            html=html
        )
        try:
            mail.send(msg)
            return "We have sent an email confirmation"
        except Exception as error:
            print(error)
            return "error"

    def get(self):
        login = request.args.get('login')
        user_id = request.args.get('id')
        doc = request.args.get('doc')
        session['login'] = login
        session['user_id'] = id
        url = "http://www.localhost:5000/doc{}?login={}&id={}".format(doc,login, user_id)
        return redirect(url, code=302)