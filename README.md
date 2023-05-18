# 帮助文档 Helper

## 安装

1. 克隆本仓库 

    ```bash
    git clone https://github.com/peacemo/DocHelper.git
    ```

2. 安装运行环境所需要的第三方库 
    
    ```bash
    python -m pip install -r requirements.txt
    ```

## 使用

1. 按照 `configs/example.yml` 模板编写函数的配置文件；

2. 运行 `python main.py [YAML 文件名]` 以生成文档；

3. 文档位于 `ouputs/` 下，与 `yml` 配置文件同名。

> 运行 `python main.py "example"` 查看示例。

## 说明

仅作初步生成用，不可完全依赖本脚本。生成效果请预览 `outputs/example.md`

## 致谢

本项目使用了以下开源项目：

- [Jinja](https://github.com/pallets/jinja) - 该项目基于 BSD-3-Clause 协议发布。

- [PyYaml](https://github.com/yaml/pyyaml) - 该软件基于 MIT 协议发布。

感谢这些优秀的开源项目，它们为我的开发工作提供了巨大的帮助。