from .connection import start_connection
from .models import Models
import time


def start_db_with_docker():
    dbstatus = True
    while dbstatus:
        try:
            start_db()
            dbstatus = False
        except:
            print("Waiting for connection to Postgres Container")
            time.sleep(2)


def start_db():
    connection, cursor = start_connection()
    # add tables
    cursor.execute(Models.users)
    cursor.execute(Models.docs)
    cursor.execute(Models.docs_users)

    cursor.execute(Models.votes)
    cursor.execute(Models.votes_users)
    cursor.execute(Models.chats)
    cursor.execute(Models.chat_docs)
    cursor.execute(Models.messages)
    cursor.execute(Models.chat_messages)


    connection.commit()
    print("Tables created successfully in PostgreSQL ")
    cursor.close()
    connection.close()
