from flask import request
from app.resources.Common.UsersCommon import UsersCommon


class UserId(UsersCommon):

    # @jwt_required
    def get(self, user_id):
        sql = """
                SELECT  u.*
                FROM users u
                WHERE u.user_id = %s
            ;"""
        record = (user_id,)
        user = self.base_get_one(sql, record)
        return user

    def delete(self, user_id):
        sql = """DELETE from users WHERE user_id = %s"""
        record = (user_id,)
        res = self.base_write(sql, record)
        return res


