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
        'email': "mr.andrey.sd@gmail.com",
        'login': 'Andrei',
        'password': password
    },
    {
        'email': "nik3.mr@gmail.com",
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

docs = ['ПАО НК Роснефть', 'ПАО РусГидро', 'ПАО Сбербанк']


def create_user(user):
    sql = """INSERT INTO   users (email, login, password)
                     VALUES (%s, %s, %s)
                    ;"""
    record = (user['email'], user['login'], user['password'])
    cursor.execute(sql, record)
    connection.commit()


def create_doc(doc):
    sql = """   INSERT INTO   docs (doc_name)
                VALUES (%s)
            ;"""
    record = (doc,)
    cursor.execute(sql, record)
    connection.commit()


def create_docs_users(doc_id, user_for_docs):
    for user_id in range(1, user_for_docs):
        sql = """   INSERT INTO  docs_users (user_id, doc_id)
                    VALUES (%s, %s)
                    ;"""
        record = (user_id, doc_id)
        cursor.execute(sql, record)
        connection.commit()

connection, cursor = start_connection()
try:
    for doc in docs:
        create_doc(doc)
    for user in users:
        create_user(user)
    for doc_id in range(1, len(docs) + 1):
        if doc_id == 1:
            user_for_docs = len(users) + 1
        elif doc_id == 2:
            user_for_docs = len(users)
        else:
            user_for_docs = len(users) - 1
        create_docs_users(doc_id, user_for_docs)


except Exception as e:
    print(e)
finally:
    close_connection(connection, cursor)
