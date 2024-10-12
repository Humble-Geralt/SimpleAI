#!/user/bin/env python
# -*-conding: utf-8 -*-
# @Time     : 2024/10/10 下午2:05
# @Author   : FelixYe
# @File     : config.py
# @Software : PyCharm
# @Project  : SimpleAI
import yaml
import os
import re
from dataclasses import dataclass, fields, is_dataclass

from simpleai.constant.path_constant import CONFIG_DIR
from simpleai.constant.model_constant import BaseModel


def replace_env_variables(value):
    pattern = re.compile(r'\$\{([^}:-]+)(?::-(.+?))?}')

    def replacer(match):
        var_name = match.group(1)
        default_value = match.group(2)
        return os.getenv(var_name, default_value if default_value is not None else '')

    return pattern.sub(replacer, value)


def env_var_constructor(loader, node):
    value = loader.construct_scalar(node)
    env_value = replace_env_variables(value)
    # Attempt to cast to appropriate type
    if env_value is not None:
        if env_value.lower() in ('true', 'false'):
            return env_value.lower() == 'true'
        try:
            return int(env_value)
        except ValueError:
            try:
                return float(env_value)
            except ValueError:
                return env_value
    return env_value


yaml.SafeLoader.add_constructor('tag:yaml.org,2002:str', env_var_constructor)


@dataclass
class SimpleAI:
    """
    Business logic configuration.

    Attributes:
        debug (bool): Whether debug mode is enabled.
    """

    debug: bool


@dataclass
class GlobalConfig:
    """
    Global configuration.

    Attributes:
        SimpleAI (SimpleAI): SimpleAI configuration.
    """
    simple_ai: SimpleAI
    base_model: BaseModel

    @classmethod
    def from_yaml(cls, file_path: str):
        with open(file_path, 'r') as f:
            config_data = yaml.safe_load(f)
        return cls._from_dict(config_data)

    @classmethod
    def _from_dict(cls, config_data: dict):
        kwargs = {}
        for field in fields(cls):
            field_name = field.name
            field_type = field.type
            if is_dataclass(field_type):
                sub_config_data = config_data.get(field_name, {})
                sub_config = field_type(**sub_config_data)
                kwargs[field_name] = sub_config
            else:
                kwargs[field_name] = config_data.get(field_name)
        return cls(**kwargs)


config_path = os.path.join(CONFIG_DIR, 'simpleai_conf.yml')

global_config = GlobalConfig.from_yaml(config_path)
