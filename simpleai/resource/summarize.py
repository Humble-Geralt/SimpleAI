#!/user/bin/env python
# -*-conding: utf-8 -*-
# @Time     : 2024/10/12 下午1:32
# @Author   : FelixYe
# @File     : summarize.py
# @Software : PyCharm
# @Project  : SimpleAI
from flask_restx import Resource, Namespace

from simpleai.configs.config import global_config
from simpleai.initizlization.model_client import client
from simpleai.prompts.summarize_prompt import summarize_prompt
from simpleai.schemas.summarize import SummarizeSchema

summarize = Namespace('Summarize', description='Summarize api')

summarize_schema = SummarizeSchema()
summarize_payload_model, summarize_response_model = summarize_schema.create_models(summarize)


class Summarize(Resource):
    @summarize.expect(summarize_payload_model)
    @summarize.marshal_with(summarize_response_model)
    def post(self):
        data = summarize.payload
        content = data['content']
        if not content:
            return {
                'status_code': 40000,
                'message': 'Missing necessary parameters, please check!'
            }
        completion = client.chat.completions.create(
            model=global_config.base_model.model_info.completion_model,
            messages=[
                {"role": "system", "content": summarize_prompt},
                {"role": "user", "content": content}
            ],
            timeout=60
        )
        res = completion.choices[0].message.content
        return {
            'content': res,
        }


summarize.add_resource(Summarize, '')
