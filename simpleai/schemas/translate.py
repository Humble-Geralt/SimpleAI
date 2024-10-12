#!/user/bin/env python
# -*-conding: utf-8 -*-
# @Time     : 2024/10/12 下午3:03
# @Author   : FelixYe
# @File     : translate.py
# @Software : PyCharm
# @Project  : SimpleAI
import uuid

from flask_restx import fields

from simpleai.schemas.base_schema import BaseSchema


class TranslateSchema(BaseSchema):

    def get_payload_fields(self):
        return {
            'current_lang': fields.String(required=False,
                                          description='The current language, if not filled in, '
                                                      'will be determined by the model itself'),
            'target_lang': fields.String(required=True, description='The target language'),
            'content': fields.String(required=True, description='The content need be correction')
        }

    def get_response_fields(self):
        return {
            'uuid': fields.String(required=True, description='The unique request ID', default=str(uuid.uuid4())),
            'status_code': fields.Integer(required=True, description='The status code', default=20000),
            'content': fields.String(required=True, description='The content after translated', default=None),
            'message': fields.String(required=True, description='message of api', default="success!")
        }
