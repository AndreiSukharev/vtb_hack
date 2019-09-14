from flask import request
from app.resources.Common.Base import Base


class Vote(Base):

    def post(self):
        vote_id = request.json['vote_id']
        user_id = request.json['user_id']
        vote = request.json['vote']
        res = self.__check_vote(vote_id, user_id)
        if not res:
            self.__add_vote(vote_id, user_id, vote)
        # elif res['']
        print(res)
        return res

    def __add_vote(self, vote_id, user_id, vote):
        pass

    def __check_vote(self, vote_id, user_id):
        sql = """
                    SELECT vote
                    FROM votes_users
                    WHERE vote_id = %s AND user_id = %s
                            ;"""
        record = (vote_id, user_id)
        res = self.base_get_limited_all(sql, record)
        return res
