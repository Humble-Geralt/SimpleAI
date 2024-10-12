#!/user/bin/env python
# -*-conding: utf-8 -*-
# @Time     : 2024/10/12 下午12:50
# @Author   : FelixYe
# @File     : translate_prompt.py
# @Software : PyCharm
# @Project  : SimpleAI
from simpleai.initizlization.model_client import client
from flask_restx import Resource, Namespace

from simpleai.configs.config import global_config
from simpleai.initizlization.model_client import client
from simpleai.prompts.translate_prompt import translate_prompt
from simpleai.schemas.translate import TranslateSchema

translate = Namespace('Translate', description='Translation api')

translate_schema = TranslateSchema()
translate_payload_model, translate_response_model = translate_schema.create_models(translate)


class Correction(Resource):
    @translate.expect(translate_payload_model)
    @translate.marshal_with(translate_response_model)
    def post(self):
        data = translate.payload
        current_lang = data['current_lang']
        target_lang = data['target_lang']
        content = data['content']
        if not target_lang:
            return {
                'status_code': 40000,
                'message': 'Missing necessary parameters, please check!'
            }

        completion = client.chat.completions.create(
            model=global_config.base_model.model_info.completion_model,
            messages=[
                {"role": "system", "content": translate_prompt.format(current_lang, target_lang, content)},
                {"role": "user", "content": data["content"]}
            ],
            timeout=60
        )
        res = completion.choices[0].message.content
        return {
            'content': res,
        }


translate.add_resource(Correction, '')
