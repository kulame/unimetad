# unimetad

unimetad 元数据管理服务器

## 本地部署

1. 环境准备

```sh
mkdir -p /data/log/{project_name}/app
virtualenv .venv -p python3.8
source .venv/bin/activate
# 创建虚拟环境，安装依赖
pip install -r requirements.txt
```


2. 启动项目


```sh
scripts/dev
```

## 本地开发

1. 安装 pre-commit/pylint/tox 依赖
2. 在本地执行 `pre-commit install`
3. 在进行代码提交(git commit)的时候，会进行代码格式校验
4. 本地执行单元测试: `tox`

## 数据/设计/版本特性文档

```sh
mkdocs serve
```


## 生成/查看API文档

```sh
npm install apidoc -g
apidoc -i api/views -o apidoc/
```