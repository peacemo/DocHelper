# 帮助文档 Helper

## 安装

1. 克隆本仓库 `git clone https://github.com/peacemo/DocHelper.git`

2. 运行 `pip install -r requirements.txt`

## 使用

必需以下文件：

* ./config/<config_name>.yml
* ./template_doc.md

yml 格式的模板位于 `./config/template.yml`， 依照模板修改其中的变量即可。

运行 `python main.py [YAML 文件名]` 以生成文档。例如 `python main.py "example"`

默认输出与 yml 配置文件同名的 md 文档。

## 说明

仅作初步生成用，不可完全依赖本脚本。