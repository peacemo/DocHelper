# 帮助文档 Helper

## 安装

1. 克隆本仓库

2. 运行 `pip install -r requirements.txt`

## 使用

必需以下文件

* ./config/<config_name>.yml
* ./template_doc.md

使用之前，在 `main.py` 中修改 `config_name` 为目标文件名，使用 `python ./main.py` 运行。

yml 格式的模板在 `./config/template.yml`， 依照模板修改其中的变量即可。

## 说明

仅作初步生成用，不可完全依赖本脚本。