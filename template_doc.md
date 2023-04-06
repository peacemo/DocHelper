# {{ function.name }}
---
{{ function.short_description }}

## 语法

```julia
{% for usage in usages %}
{% for name in usage.outputs %}{{ name.name }}, {% endfor %}= {{ function.name }}({% for name in usage.inputs %}{{ name.name }}, {% endfor %})
{% endfor %}
```

## 说明
{% set comma = "" %} 
{% for usage in usages %}
{% for name in usage.outputs %}[{{ name.name }}](/Doc/{{ tool_box }}/{{ class }}/{{ sub_class }}/{{ function.name }}.html#{{ name.name }}), {% endfor %}= {{ function.name }}({% for name in usage.inputs %}[{{ name.name }}](/Doc/{{ tool_box }}/{{ class }}/{{ sub_class }}/{{ function.name }}.html#{{ name.name }}), {% endfor %}) {{ usage.usage }}
{% endfor %}
## 示例
{% for example in examples %}
<div id="{{ example.name }}" class="jump-target"></div>
<div class="details-box">
<details open>
<summary>{{ example.name }}</summary>
</details>
<div class="details-content">

示例内容

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
