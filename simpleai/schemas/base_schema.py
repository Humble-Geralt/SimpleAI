#!/user/bin/env python
# -*-conding: utf-8 -*-
# @Time     : 2024/10/12 下午2:09
# @Author   : FelixYe
# @File     : base_schema.py
# @Software : PyCharm
# @Project  : SimpleAI
import uuid

from flask_restx import fields


class BaseSchema:
    def create_models(self, api):
        """when child init the property, use it to build the payload and repose"""
        # payload
        user_payload_model = api.model('UserInput', self.get_payload_fields())

        # response
        user_response_model = api.model('UserResponse', self.get_response_fields())

        return user_payload_model, user_response_model

    def get_payload_fields(self):
        """Implement this method"""
        raise NotImplementedError("Subclasses must implement 'get_input_fields' method.")

    def get_response_fields(self):
        """Implement this method"""
        raise NotImplementedError("Subclasses must implement 'get_response_fields' method.")
