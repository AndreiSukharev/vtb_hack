class Models:
    users = '''
                CREATE TABLE IF NOT EXISTS users(
                user_id         SERIAL          NOT NULL PRIMARY KEY,
                email           VARCHAR(64)     UNIQUE,
                login           VARCHAR (64)    NOT NULL UNIQUE,
                password        VARCHAR(1024),
                online          BOOLEAN         DEFAULT '0',
                room            TEXT[]
                );'''

    docs = '''
             CREATE TABLE IF NOT EXISTS docs(
             doc_id         SERIAL          NOT NULL PRIMARY KEY,
             doc_name       VARCHAR(64)     NOT NULL,
             creationDate   INT
             );'''

    docs_users = '''
                CREATE TABLE IF NOT EXISTS docs_users(
                 user_id     INT REFERENCES users (user_id) ON DELETE CASCADE,
                 doc_id     INT REFERENCES docs (doc_id) ON DELETE CASCADE
                );'''
    docs_votes = '''
                CREATE TABLE IF NOT EXISTS docs_votes(
                 vote_id     INT REFERENCES votes (vote_id) ON DELETE CASCADE,
                 doc_id     INT REFERENCES docs (doc_id) ON DELETE CASCADE
                );'''

    votes = '''
                CREATE TABLE IF NOT EXISTS votes(
                vote_id        SERIAL   NOT NULL PRIMARY KEY,
                vote_text      TEXT     NOT NULL,
                plus           INT      DEFAULT 0,
                minus          INT      DEFAULT 0
            );'''

    votes_users = '''
                CREATE TABLE IF NOT EXISTS votes_users(
                 vote_id     INT REFERENCES votes (vote_id) ON DELETE CASCADE,
                 user_id     INT REFERENCES users (user_id) ON DELETE CASCADE
                );'''


    chats = '''
                CREATE TABLE IF NOT EXISTS chats(
                chat_id        SERIAL          NOT NULL PRIMARY KEY,
                chat_name      VARCHAR(64)     NOT NULL,
                vote_id  INT REFERENCES votes (vote_id) ON DELETE CASCADE
                );'''


    chat_messages = '''
                CREATE TABLE IF NOT EXISTS chat_messages(
                 chat_id     INT REFERENCES chats (chat_id) ON DELETE CASCADE,
                 message_id  INT REFERENCES messages (message_id) ON DELETE CASCADE
                );'''

    messages = '''
                 CREATE TABLE IF NOT EXISTS messages(
                 message_id     SERIAL          NOT NULL PRIMARY KEY,
                 creation_date  VARCHAR(64)     NOT NULL,
                 text           TEXT            NOT NULL,
                 author         INT             NOT NULL REFERENCES users(user_id) ON DELETE CASCADE
                 );'''