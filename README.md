# 帮助文档 Helper

本项目用于初步生成函数的帮助文档。专注配置文件的编写，而无需在意格式。

通过对配置文件进行一对一填充，自动生成初步的带有格式和超链接的文档。作为一个帮助文档的 startup 再好不过。

通过 10 分钟的学习，即可为后续工作带来很大的效率提升。使用本项目，一个得当的 yaml 配置文件可以生成 80% 的函数文档，节省大量的反复 ~~复制粘贴~~ 的工作。

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

> 运行 `python main.py "example"` 查看示例。

1. 按照 [`configs/example.yml`](./configs/example.yml) 模板编写函数文档的配置文件；

2. 运行 `python main.py [YAML 文件名]` 以生成文档；

3. 文档位于 `ouputs/` 下，与 `yml` 配置文件同名。

> 使用前可以先阅读本文档最后一节 **注意事项**。

效果：

![](./DocHelper.gif)

## 模板内容

初步生成的模板包含以下内容，也可直接查看 [`outputs/example.md`](./outputs/example.md)：

- 函数标题

- 语法

    多个语法支持：
    ```julia
     mdl, = AdaboostTree(X, )
     mdl, = AdaboostTree(____, Name=Value, )
    ```

- 说明

    基于**语法**小结自动生成说明，包含变量的超链接生成。

    效果（此说明文档中的连接不可跳转，仅作展示用）：

    [output_0](/Doc/ToolBoxName/ClassName/SubClassName/function_name.html#output_0), = function_name([input_0](/Doc/ToolBoxName/ClassName/SubClassName/function_name.html#input_0), ) 这个函数的详细介绍就写在这里，对应的就是网页版本中，说明栏目每一个用法后面的详细文字说明。如果文字需要换行，使用 `\n\n` 来进行换行。

    比如说这样。
    *****

    [output_0](/Doc/ToolBoxName/ClassName/SubClassName/function_name.html#output_0), = function_name([____](/Doc/ToolBoxName/ClassName/SubClassName/function_name.html#输入参数), [Name=Value](/Doc/ToolBoxName/ClassName/SubClassName/function_name.html#名称-值对组参数), ) 这个说明只是一个示例，现在是第二种用法的说明。这里就介绍一下 `Name=Value` 的配置规范。
    *****

- 示例

    自动生成可展开-收起的 HTML 语法示例，模板中可包含示例的名称，可包含多个示例（见 example.yml/example.md）: 

    ```html
   <div id="用例的标题" class="jump-target"></div>
    <div class="details-box">
    <details open>
    <summary>用例的标题</summary>
    </details>
    <div class="details-content">

    示例内容，使用 *Markdown* 格式文本进行编写。

      </div>  
    </div>
    ```
- 输入参数

    根据 `yml` 模板自动生成多条可展开-收起的 HTML 输入参数: 

    ```julia
    <div id="input_0" class="jump-target"></div>
    <div class="details-box">
    <details open>
    <summary>input_0 - 第一个输入参数<div>一个类型</div></summary>
    </details>
    <div class="details-content">

    这里是第一个参数的详细文字介绍，这里的参数和上面 `usages -> usage -> inputs -> name` 里面的参数一致哈。

    **数据类型:**  Dataframe

      </div>
    </div>
    ```

- 名称-值对组参数
    
    与输入参数功能相同，包含默认值。

- 输出参数

    与输入参数功能相同。

## 致谢

本项目使用了以下开源项目：

- [Jinja](https://github.com/pallets/jinja) - 该项目基于 BSD-3-Clause 协议发布。

- [PyYaml](https://github.com/yaml/pyyaml) - 该软件基于 MIT 协议发布。

感谢这些优秀的开源项目，它们为我的开发工作提供了巨大的帮助。

## 注意事项

> 仅作初步生成用，不可完全依赖本脚本。生成效果请预览 `outputs/example.md`

- 用法小结

    用法中一般的参数写在 `usages -> usage -> outputs/inputs -> name` 中，模板将自动将其整理为 `out = function_name(input)` 形式，并分别展示在**语法**和**说明**中。其中，**说明**板块的用法还包含变量说明的跳转超链接。

    用法中的 *名称-值对组* 参数使用固定的字符串表示，即 `Name=Value`，其位置与一般参数无异，见 `example.yml`. 

    用法中与 *名称-值对组* 参数搭配的表示所有一般输入参数使用 “`____`” 表示。

    一个包含了 *名称-值对组* 参数的设定示例如下：

    ```yml
    usages:  
        - usage: "用法的说明"  
        outputs:  
            - name: "out_0"  
            - name: "out_1"
        inputs:  
            - name: "input_0"
            - name: "input_1"
        - usage: "用法二的说明"
        outputs: 
            - name: "out_0"  
            - name: "out_1"
        inputs:  
            - name: "____"  
            - name: "Name=Value" 
    ```

    最终生成的函数用法语句中，最后一个参数后有多余的 "`, `" 需要手动进行删除。

- 参数小结

    在用法中出现的带有具体名称的参数，在后续中的参数详细说明中**必须出现**，否则超链接将无法定位。比如在上面我们指定了 `out_0, out_1, input_0, input_1` 以及 `Name=Value` 参数。在 `yml` 配置文件中，需要对 `out_0, out_1, input_0, input_1` 在详细位置做说明。如果**用法**中存在而**参数**中不存在，模板自动生成的超链接将指向一个空页面。

    而实际算法中可选的 `Name=Value` 参数无需在**用法**中给出，只需在 `yml` 中的 `name_value:` 配置中按模板示例给出即可。

- 示例小结

    请注意，目前的模板中，并不支持处理带有空格的 `div` 板块，因此，在 `yml` 中的 `examples -> example -> name` 配置项中不要出现空格。
