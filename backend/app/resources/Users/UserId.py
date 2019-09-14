from app.resources.Common.Base import Base


class UserId(Base):

    def get(self, user_id):
        sql = """
                SELECT * from users
                WHERE user_id= %s
            ;"""
        record = (user_id,)
        user = self.base_get_one(sql, record)
        return user

    def delete(self, user_id):
        sql = """DELETE from users WHERE user_id = %s"""
        record = (user_id,)
        res = self.base_write(sql, record)
        return res

