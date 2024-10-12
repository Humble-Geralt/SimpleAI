#!/user/bin/env python
# -*-conding: utf-8 -*-
# @Time     : 2024/10/11 下午3:59
# @Author   : FelixYe
# @File     : model_client.py
# @Software : PyCharm
# @Project  : SimpleAI
from simpleai.configs.config import global_config
from simpleai.initizlization.log import get_logger
from openai import OpenAI

logger = get_logger(__name__)


class CustomClient:
    # custom client when not support OPENAI SDK
    ...


if global_config.base_model.model_info.get_openai_sdk_supported():
    client = OpenAI(
        api_key=global_config.base_model.model_info.api_key,
        base_url=global_config.base_model.model_info.base_url,
    )
    logger.info(f"OPENAI SDK initialization success! current model is "
                f"{global_config.base_model.model_info.completion_model}")
else:
    try:
        # use http
        client = CustomClient()
        ...
    except Exception as e:
        logger.error(f"model client ")


if __name__ == '__main__':
    completion = client.chat.completions.create(
        model=global_config.base_model.model_info.completion_model,
        messages=[
            {"role": "system", "content": "你是一个专业的中英翻译，需要你将以下中文翻译为英文."},
            {"role": "user", "content": "多家银行明确，存量房贷利率调整将由银行统一进行批量调整，不需要客户提出申请"}
        ]
    )

    print(completion.choices[0].message)
