#!/user/bin/env python
# -*-conding: utf-8 -*-
# @Time     : 2024/10/12 下午4:01
# @Author   : FelixYe
# @File     : gunicorn_config.py.py
# @Software : PyCharm
# @Project  : SimpleAI
# gunicorn_config.py

bind = '0.0.0.0:5000'

workers = 4

loglevel = 'info'

timeout = 120
