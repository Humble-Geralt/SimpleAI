#!/user/bin/env python
# -*-conding: utf-8 -*-
# @Time     : 2024/10/10 下午2:03
# @Author   : FelixYe
# @File     : path_constant.py
# @Software : PyCharm
# @Project  : SimpleAI
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
LOG_DIR = os.path.join(ROOT_DIR, 'log')
CONFIG_DIR = os.path.join(ROOT_DIR, 'configs')
