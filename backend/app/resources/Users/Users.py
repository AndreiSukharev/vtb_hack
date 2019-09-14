from app.resources.Common.Base import Base
from flask import request, session
from flask_jwt_extended import jwt_required


class Users(Base):

    # @jwt_required
    def get(self):
        sql = """
                SELECT  u.*
                FROM users u
            ;"""
        users = self.base_get_all(sql)
        return users

    # @jwt_required
    # def post(self):
    #     email = request.json['email']
    #     login = request.json['login']
    #     password = request.json['password']
    #
    #     record = (email, login, password)
    #     sql = '''INSERT INTO users (email, login, password)
    #              VALUES (%s, %s, %s);'''
    #     res = self.base_write(sql, record)
    #     return res
