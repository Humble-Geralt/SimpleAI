#!/user/bin/env python
# -*-conding: utf-8 -*-
# @Time     : 2024/10/12 下午1:32
# @Author   : FelixYe
# @File     : correction.py
# @Software : PyCharm
# @Project  : SimpleAI
from flask_restx import Resource, Namespace

from simpleai.configs.config import global_config
from simpleai.initizlization.model_client import client
from simpleai.prompts.correction_prompt import correction_prompt
from simpleai.schemas.correction import CorrectionSchema

correction = Namespace('Correction', description='Error correction api')

correction_schema = CorrectionSchema()
correction_payload_model, correction_response_model = correction_schema.create_models(correction)


class Correction(Resource):
    @correction.expect(correction_payload_model)
    @correction.marshal_with(correction_response_model)
    def post(self):
        data = correction.payload
        content = data['content']
        if not content:
            return {
                'status_code': 40000,
                'message': 'Missing necessary parameters, please check!'
            }
        completion = client.chat.completions.create(
            model=global_config.base_model.model_info.completion_model,
            messages=[
                {"role": "system", "content": correction_prompt},
                {"role": "user", "content": content}
            ],
            timeout=60
        )
        res = completion.choices[0].message.content
        return {
            'content': res,
        }


correction.add_resource(Correction, '')
