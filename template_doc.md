# {{ function.name }}
---
{{ function.short_description }}

## 语法

```julia{% for usage in usages %}
{% for name in usage.outputs %}{{ name.name }}, {% endfor %}= {{ function.name }}({% for name in usage.inputs %}{{ name.name }}, {% endfor %}){% endfor %}
```

## 说明
{% for usage in usages %}
{% for name in usage.outputs %}[{{ name.name }}](/Doc/{{ tool_box }}/{{ class }}/{{ sub_class }}/{{ function.name }}.html#{{ name.name }}), {% endfor %}= {{ function.name }}({% for name in usage.inputs %}[{{ name.name }}](/Doc/{{ tool_box }}/{{ class }}/{{ sub_class }}/{{ function.name }}.html#{% if name.name=="Name=Value"%}{{ "名称-值对组参数" }}{% else %}{{ name.name }}{% endif %}), {% endfor %}) {{ usage.usage }}
*****
{% endfor %}
## 示例
{% for example in examples %}
<div id="{{ example.name }}" class="jump-target"></div>
<div class="details-box">
<details open>
<summary>{{ example.name }}</summary>
</details>
<div class="details-content">

示例内容，使用 *Markdown* 格式文本进行编写。

  </div>
</div>
{% endfor %}

## 输入参数
{% for arg in inputs %}
<div id="{{ arg.arg }}" class="jump-target"></div>
<div class="details-box">
<details open>
<summary>{{ arg.arg }} - {{ arg.short_description }}<div>{{ arg.type_zh }}</div></summary>
</details>
<div class="details-content">

{{ arg.long_description }}

**数据类型:**  {{ arg.type }}

  </div>
</div>
{% endfor %}
{% if name_value %}
### 名称-值对组参数

指定可选的、以逗号分隔的 Key=Value 对组参数。Key 为参数名称，Value 为对应的值。您可采用任意顺序指定多个名称-值对组参数，如 Key1=Value1,...,KeyN=ValueN 所示。

**示例：**

{% for arg in name_value %}
<div id="{{ arg.arg }}" class="jump-target"></div>
<div class="details-box">
<details open>
<summary>{{ arg.arg }} - {{ arg.short_description }}<div>{{ arg.default}} （默认） | {{ arg.type_zh }}</div></summary>
</details>
<div class="details-content">

{{ arg.long_description }}

**数据类型:**  {{ arg.type }}

  </div>
</div>
{% endfor %}
{% endif %}

## 输出参数
{% for arg in outputs %}
<div id="{{ arg.arg }}" class="jump-target"></div>
<div class="details-box">
<details open>
<summary>{{ arg.arg }} - {{ arg.short_description }}<div>{{ arg.type_zh }}</div></summary>
</details>
<div class="details-content">

{{ arg.long_description }}

  </div>
</div>
{% endfor %}
