from flask import request
from app.resources.Common.Base import Base
from .Email import Email
import datetime


class Docs(Base):

    def get(self):
        sql = """
                SELECT  *
                FROM docs
            ;"""
        docs = self.base_get_all(sql)
        return docs

    def post(self):
        try:
            cur_time = datetime.datetime.now().timestamp()
            doc_id = request.json['doc_id']
            sql = """UPDATE docs SET creationDate = %s
                    WHERE doc_id = %s
                    ;"""
            record = (cur_time, doc_id)
            self.base_write(sql, record)
            self.__send_emails(doc_id)
            return "ok"
        except Exception as e:
            print(e)
            return e

    def __send_emails(self, doc_id):
        users = [
            {
                'email': "mr.andrey.sd@gmail.com",
                'login': 'Andrei',
                'id': 1
            },
            {
                'email': "nik3.mr@gmail.com",
                'login': 'Artem',
                'id': 2
            },
            {
                'email': "vladisslaww@gmail.com",
                'login': 'Vladislav',
                'id': 3
            },
            {
                'email': "juliarychkova1@gmail.com",
                'login': 'Julia',
                'id': 4
            },
            {
                'email': "curetoyou@gmail.com",
                'login': 'Vova',
                'id': 5
            },
            {
                'email': "innmaster38@gmail.com",
                'login': 'Master',
                'id': 6
            },
        ]
        for user in users:
            Email.send_email_votes(user['email'], user['login'], user['id'], doc_id)