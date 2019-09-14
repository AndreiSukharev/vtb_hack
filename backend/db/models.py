class Models:
    users = '''
                CREATE TABLE IF NOT EXISTS users(
                user_id         SERIAL          NOT NULL PRIMARY KEY,
                user_name       VARCHAR(64)     NOT NULL
                );'''
