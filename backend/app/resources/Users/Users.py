from app.resources.Common.Base import Base
from flask import request


class Users(Base):

    def get(self):
        sql = """
                SELECT  * from users
            ;"""
        users = self.base_get_all(sql)
        return users

    def post(self):
        name = request.json['user_name']
        record = (name,)
        sql = '''INSERT INTO users (user_name)
                 VALUES (%s);'''
        res = self.base_write(sql, record)
        return res
