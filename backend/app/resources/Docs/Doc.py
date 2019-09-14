from flask import request
from app.resources.Common.Base import Base
import datetime


class Doc(Base):

    def get(self, doc_id):
        sql = """
                SELECT  *
                FROM docs
                WHERE doc_id = %s
            ;"""
        record = (doc_id,)
        doc = self.base_get_one(sql, record)
        return doc

    def post(self):
        try:
            cur_time = datetime.datetime.now().timestamp()
            doc_id = request.json['doc_id']
            print(cur_time)
            # sql = """INSERT INTO docs (creationDate)
            #         VALUES (%s)
            #         WHERE doc_id = %s
            #         ;"""
            # record = (cur_time, doc_id)
            # self.base_write(sql, record)
            return "ok"
        except Exception as e:
            print(e)
            return e


