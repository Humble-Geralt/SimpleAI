#!/user/bin/env python
# -*-conding: utf-8 -*-
# @Time     : 2024/10/10 下午2:20
# @Author   : FelixYe
# @File     : model_constant.py
# @Software : PyCharm
# @Project  : SimpleAI
from dataclasses import dataclass, asdict
from typing import Union


@dataclass
class ModelConstants:
    """
    Base class for all model constants
    """
    _OPENAI_SDK_SUPPORTED: bool = False

    def get_openai_sdk_supported(self) -> bool:
        return self._OPENAI_SDK_SUPPORTED


@dataclass
class ChatGPT(ModelConstants):
    """
    GPT model related constants

    Attributes:
        api_key (str): API key for GPT
        completion_model (str): Completion model
        base_url (str): Base URL for GPT
    """
    api_key: str = None
    completion_model: str = 'gpt-3.5-turbo'
    base_url: str = 'https://api.openai.com/v1'
    # embedding_model: str = 'text-embedding-3-small'

    _OPENAI_SDK_SUPPORTED: bool = True


@dataclass
class Qwen(ModelConstants):
    """
    Qwen model related constants

    Attributes:
        api_key (str): API key for Qwen
        completion_model (str): Completion model
        base_url (str): Base URL for Qwen
        completion_endpoint (str): if using http not SDK，need this url as completion endpoint
    """
    api_key: str = None
    completion_model: str = 'qwen-plus'
    base_url: str = 'https://dashscope.aliyuncs.com/compatible-mode/v1'
    completion_endpoint: str = 'https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions'

    _OPENAI_SDK_SUPPORTED: bool = True


@dataclass
class BaseModel:
    """
    Base model settings

    Attributes:
        model_info (Union[chatGPT, ...]): The base model configuration, which can be either chatGPT or other.
    """
    model_type = str
    model_info: Union[ChatGPT, Qwen, None] = None

    def __init__(self, **model_info: dict):
        if len(model_info["model_type"].split(",")) != 1:
            raise ValueError("base model should have only one type.")

        self.model_type = model_info["model_type"].lower()
        model_info.pop("model_type", None)
        model_config = model_info

        if self.model_type == "chatgpt":
            self.model_info = ChatGPT(**model_config)
        elif self.model_type == "qwen":
            self.model_info = Qwen(**model_config)
        else:
            raise TypeError("Non-supported base model type")

    def to_dict(self):
        return asdict(self.model_info)
