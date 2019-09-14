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
users = []


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
