## 项目概览
SimpleAI是一个简易的flask后端项目，通过调用大模型完成翻译、总结等功能，通过API的方式提供服务。
SimpleAI通过分层设计和环境变量配置支持可拓展的基座模型替换和功能重写、新增。凡是支持OPENAI_SDK的大模型服务均可以直接接入。
项目正在完善中。
## 接口情况
模版中提供了三个功能接口，分别为纠错、总结和翻译。
具体的接口说明可以通过启动服务后的swaggerUI查看和测试。

可以通过 http://127.0.0.1:5000/api/ 查看具体的接口和用法

通过flask_restx实现便利的接口参数校验和OPENAPI生成。
OPENAPI:http://127.0.0.1:5000/api/swagger.json
## 项目启动
对于开发和调试可以直接通过根目录内的app.py启动
```language
python app.py
```
对于生产环境可以参考根目录下的Dockerfile文件进行打包，默认使用gunicorn启动
```language
#镜像打包
docker build -t simpleai .
```
## 配置读取
通过直接读取环境变量来进行配置，同时有默认配置。
启动时通过按照模版env文件进行修改后启动，docker可参考
```language
docker run --env-file .env -p 5000:5000 simpleai
```


