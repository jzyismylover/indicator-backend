# 代码使用

从项目整体结构来说，基于python flask 框架搭建 restful api。启动文件为 `setup.py`

从目录来说，包括 config、resources、utils、static

## 启动项目

项目基于 python3.7 开发，因此需要具备 python 环境。主目录下有 requirements.txt，可通过以下代码下载项目所需要使用的包

```bash
$ pip install -r requirements.txt
```

主目录下有一个`database.yml`文件，主要用于docker-compose启动mysql、redis

```bash
$ docker-compose -f database.yml up -d
```

不使用docker-compose的话也可以自行安装mysql / redis 到本地，然后在 config 配置处修改对应的用户名和密码即可。

```bash
$ set FLASK_APP=setup
$ set FLASK_DEBUG=true
$ flask run --host=0
```



## config

config 目录下主要是一些工具的配置文件。包括 sqlalchemy、redis、celery、flask-mail、flask-apscheduler。config.yml 这个文件包含了所有工具的配置文件(区分开发环境和生产环境)，部分配置如下所示：

```python
de_db:
  hostname: localhost
  username: root
  password: jzyismylover
  port: 5006
  dbname: base
pd_db:
  hostname: mysql
  username: root
  password: jzyismylover
  port: 3306
  dbname: indicator
...
```

__init\__.py 文件向外导出所有配置的启动函数以及提供 init_enviro 初始化整个项目的环境变量。



## resources

resources 目录下是整个项目的 api 所在，即相应的接口。基本上每个目录都包含两个文件 —— _\_init_\_.py， views.py 。views.py 是接口的主要逻辑所在，_\_init_\_.py 用于注册views.py提供的接口。下面将逐一介绍各个目录对应的接口详情。

### common_indicator

该目录主要提供通用指标提取接口

![image-20230512104329626](E:\杂七杂八的东西\typeorm 图片存储区\image-20230512104329626.png)

​        如上即为一个接口，其他以此类推。目前对于通用指标采用了 redis hash 缓存的策略——对处理文本生成 md5 hash，以 md5 hash 作为键值，文本处理结果作为 value 存入 redis。这样的好处是在实际提取一个文本不同指标的时候不需要重新对文本进行处理。具体的实现逻辑在 `getParams` 函数。

​        common_indicator 里面有一个 util 目录，目录下包括一个指标提取类 `CommonIndicatorHandler` —— 包含所有指标的计算函数

### en_readability

该目录主要提供西方语种文本可读性提取接口，views.py 总体结构与 common_indicator 类似。对应也同样存在一个 util 目录包含具体可读性指标实现。



### multitask

该目录主要处理任务中心、多文档上传模块，包含任务获取、任务详情、任务下载等接口。任务即在多文档上传模块新建的处理。

如下是多文档上传的处理代码，基于 celery 框架实现计算密集任务在后台进程运行，运行完成后将结果导出到用户配置的邮箱中，相关变量可查看文件了解详情 `mutitask/views.py`。

```python
@celery.task(name='parse_files')
def parse_files(files, email):
    files = json.loads(files)
    lis = []
    for file in files:
        file = json.loads(file)
        filename = file['filename']
        contentType = file['content_type']
        data = bytes.fromhex(file['data'])
        file_storage = FileStorage(BytesIO(data), filename, content_type=contentType)
        lg_type, lg_content = language_ins.parse_file(file_storage)

        model = CommonIndicatorHandler(lg_content, lg_type)
        ans = dict()
        ans['filename'] = filename
        ans['content'] = ' '.join(model.words)
        
        # 计算指定指标
        indicators = COMMON_INDICATOR_HANDLER_MAPPING.keys()
        for _ in indicators:
            if _ not in COMMON_INDICATOR_HANDLER_MAPPING:
                continue
            func = getattr(model, COMMON_INDICATOR_HANDLER_MAPPING[_], None)
            score = func()
            ans[_] = score

        lis.append(ans)

    try:
        # 发送结果附件到邮箱
        wb = generateBinaryExcelData(lis, indicators)
        output = BytesIO()
        wb.save(output)
        output.seek(0)
        message = Message(subject='指标提取结果', body=f'请在附件查收指标提取结果', recipients=[email])
        filename = f'{uuid.uuid4().__repr__()[6:-3]}.xlsx'
        message.attach(filename, 'application/octet-stream', output.read())
        mail.send(message)
        return json.dumps(make_success_response(data=lis))
    except Exception as e:
        return {'error': str(e)}
```



### open_interace

该目录主要提供开放 api 接口（方便定制场景应用）。



### zh_readbility

该目录主要提供中文文本可读性接口。

- feature_bean：对应特征值提取实现函数
- get_features：特征提取函数（调用 feature_bean）
- method：对应方法处理类
- read_write_txt：得到特征提取依赖的数据项

`data_loader.py` 是数据初始化模块，挂载文本处理结果和对应方法处理类



## utils

​        utils 目录主要包含各个语种的文本处理函数，useForChineseInstance 即为中文文本处理函数，其余以此类推。



## static

