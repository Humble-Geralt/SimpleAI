#!/user/bin/env python
# -*-conding: utf-8 -*-
# @Time     : 2024/10/12 下午1:49
# @Author   : FelixYe
# @File     : summarize.py
# @Software : PyCharm
# @Project  : SimpleAI
import uuid

from flask_restx import fields

from simpleai.schemas.base_schema import BaseSchema


class SummarizeSchema(BaseSchema):

    def get_payload_fields(self):
        return {
            'content': fields.String(required=True, description='The content need be summarize')
        }

    def get_response_fields(self):
        return {
            'uuid': fields.String(required=True, description='The unique request ID', default=str(uuid.uuid4())),
            'status_code': fields.Integer(required=True, description='The status code', default=20000),
            'content': fields.String(required=True, description='The content after summarized', default=None),
            'message': fields.String(required=True, description='message of api', default="success!")
        }
