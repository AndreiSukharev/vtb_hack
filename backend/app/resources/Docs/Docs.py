from flask import request
from app.resources.Common.Base import Base


class Docs(Base):

    def get(self):
        sql = """
                SELECT  *
                FROM docs
            ;"""
        docs = self.base_get_all(sql)
        return docs


