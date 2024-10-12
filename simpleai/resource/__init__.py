#!/user/bin/env python
# -*-conding: utf-8 -*-
# @Time     : 2024/10/12 下午1:30
# @Author   : FelixYe
# @File     : __init__.py.py
# @Software : PyCharm
# @Project  : SimpleAI
from flask import Blueprint
from flask_restx import Api

from simpleai.resource.correction import correction
from simpleai.resource.translate import translate
from simpleai.resource.summarize import summarize

# blueprint
simpleai = Blueprint('api', __name__)
# associate blueprint and Api
simpleai_api = Api(simpleai, version='1.0', title='Simple AI')

# register namespace&resource
simpleai_api.add_namespace(correction, path='/correction')
simpleai_api.add_namespace(translate, path='/translate')
simpleai_api.add_namespace(summarize, path='/summarize')
