from flask import request
from app.resources.Common.Base import Base


class Vote(Base):

    def post(self):
        vote_id = request.json['vote_id']
        user_id = request.json['user_id']
        vote = request.json['vote']
        res = self.__check_vote(vote_id, user_id)
        if not res:
            self.__add_votes_users(vote_id, user_id, vote)
            self.__add_vote(vote_id, vote)
        elif res['vote'] != vote:
            self.__change_votes_users(vote_id, user_id, vote)
            self.__change_vote(vote_id, vote)
        return res

    def __add_vote(self, vote_id, vote):
        if vote == -1:
            sql = "UPDATE votes SET  minus = minus + 1 WHERE vote_id = %s"
        else:
            sql = "UPDATE votes SET  plus = plus + 1 WHERE vote_id = %s"
        record = (vote_id,)
        self.base_write(sql, record)

    def __change_vote(self, vote_id, vote):
        if vote == -1:
            sql = "UPDATE votes SET  minus = minus + 1, plus = plus - 1  WHERE vote_id = %s"
        else:
            sql = "UPDATE votes SET  plus = plus + 1, minus = minus - 1 WHERE vote_id = %s"
        record = (vote_id,)
        self.base_write(sql, record)

    def __change_votes_users(self, vote_id, user_id, vote):
        sql = "UPDATE votes_users SET  vote = %s WHERE user_id =%s AND vote_id = %s"
        record = (vote, user_id, vote_id)
        self.base_write(sql, record)

    def __add_votes_users(self, vote_id, user_id, vote):
        sql = '''   INSERT INTO votes_users (vote_id, user_id, vote)
                            VALUES (%s, %s, %s);'''
        record = (vote_id, user_id, vote)
        self.base_write(sql, record)

    def __check_vote(self, vote_id, user_id):
        sql = """
                    SELECT vote
                    FROM votes_users
                    WHERE vote_id = %s AND user_id = %s
                            ;"""
        record = (vote_id, user_id)
        res = self.base_get_one(sql, record)
        return res
