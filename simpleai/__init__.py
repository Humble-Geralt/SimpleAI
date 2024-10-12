#!/user/bin/env python
# -*-conding: utf-8 -*-
# @Time     : 2024/10/12 下午1:13
# @Author   : FelixYe
# @File     : __init__.py
# @Software : PyCharm
# @Project  : SimpleAI
from flask import Flask
from simpleai.configs.config import global_config
from simpleai.resource import simpleai


def create_app():
    app = Flask(__name__)

    # load config
    app.config.from_object(global_config)

    # register blueprint
    app.register_blueprint(simpleai, url_prefix='/api')

    # other init
    # db.init_app(app) 等

    return app
