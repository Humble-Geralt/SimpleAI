#!/user/bin/env python
# -*-conding: utf-8 -*-
# @Time     : 2024/10/10 下午2:02
# @Author   : FelixYe
# @File     : log.py
# @Software : PyCharm
# @Project  : SimpleAI
import logging
import os
from datetime import datetime
from simpleai.constant.path_constant import LOG_DIR
from simpleai.configs.config import global_config

IS_DEBUG = global_config.simple_ai.debug


def get_logger(name: str):
    logger = logging.getLogger(name)

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_path = os.path.join(LOG_DIR, f'log_{timestamp}.log')
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    if not IS_DEBUG:
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.DEBUG)

    stream_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(stream_formatter)
    logger.addHandler(stream_handler)

    return logger
