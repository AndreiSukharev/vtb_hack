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



