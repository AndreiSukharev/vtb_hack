from app.resources.Common.Base import Base
from flask import session
from flask_jwt_extended import get_raw_jwt, jwt_required


class LogOut(Base):

    def delete(self, user_id):
        try:
            session['login'] = ''
            session['user_id'] = ''
            # jti = get_raw_jwt()['jti']
            # sql = "INSERT INTO token_revokes (token) VALUES (%s);"
            # record = (jti,)
            # res = self.base_write(sql, record)
            # return res
            return "ok"
        except Exception as e:
            print("logout", e)

