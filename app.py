#!/user/bin/env python
# -*-conding: utf-8 -*-
# @Time     : 2024/10/12 下午1:13
# @Author   : FelixYe
# @File     : app.py.py
# @Software : PyCharm
# @Project  : SimpleAI
from simpleai import create_app

app = create_app()

if __name__ == "__main__":
    app.run(
        debug=True
    )
