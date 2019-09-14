import hashlib
import psycopg2
import psycopg2.extras
from flask import session
from app.app import app
from db.database_config import Database
from db.connection import start_connection, close_connection
from app.resources.Common.UsersCommon import UsersCommon

# from app.resources.Users.UserId import UserId


password = UsersCommon.to_hash('123Wertyq')
users = [
    {
        'email': "mr.andrey.sd@mail.ru",
        'login': 'Andrei',
        'password': password
    },
    {
        'email': "nik3.mr@mail.ru",
        'login': 'Artem',
        'password': password
    },
    {
        'email': "vladisslaww@gmail.com",
        'login': 'Vladislav',
        'password': password
    },
    {
        'email': "juliarychkova1@gmail.com",
        'login': 'Julia',
        'password': password
    },
    {
        'email': "curetoyou@gmail.com",
        'login': 'Vova',
        'password': password
    },
    {
        'email': "innmaster38@gmail.com",
        'login': 'Master',
        'password': password
    },
]


def create_user(user):
    sql = """INSERT INTO   users (email, login, password)
                     VALUES (%s, %s, %s)
                    ;"""
    record = (user['email'], user['login'], user['password'])
    cursor.execute(sql, record)
    connection.commit()

i = 0
connection, cursor = start_connection()
try:
    for user in users:
        i += 1
        create_user(user)


except Exception as e:
    print(e)
finally:
    close_connection(connection, cursor)
