from flask import request, send_file
from app.resources.Common.Base import Base


class Report(Base):

    def get(self):
        return send_file('report.txt', attachment_filename='report.txt')



