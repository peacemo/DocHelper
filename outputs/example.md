# AdaboostTree
---
阿达分类树模型

## 语法

```julia
mdl, = AdaboostTree(X, )
mdl, = AdaboostTree(____, Name=Value, )
```

## 说明

[mdl](/Doc/TyMachinelearning/Classification/Classifierensemble/AdaboostTree.html#mdl), = AdaboostTree([X](/Doc/TyMachinelearning/Classification/Classifierensemble/AdaboostTree.html#X), ) 返回基于输入数据 X 和弱模型基数 n_estimators 的阿达分类树模型。如果文字需要换行，使用 `\n\n` 

来进行换行。
*****

[mdl](/Doc/TyMachinelearning/Classification/Classifierensemble/AdaboostTree.html#mdl), = AdaboostTree([____](/Doc/TyMachinelearning/Classification/Classifierensemble/AdaboostTree.html#输入参数), [Name=Value](/Doc/TyMachinelearning/Classification/Classifierensemble/AdaboostTree.html#名称-值对组参数), ) 返回基于输入数据 X 和弱模型基数 n_estimators 的阿达分类树模型。
*****

## 示例

<div id="训练判别分析模型" class="jump-target"></div>
<div class="details-box">
<details open>
<summary>训练判别分析模型</summary>
</details>
<div class="details-content">

示例内容，使用 *Markdown* 格式文本进行编写。

  </div>
</div>


## 输入参数

<div id="X" class="jump-target"></div>
<div class="details-box">
<details open>
<summary>X - 预测数据<div>Dataframe</div></summary>
</details>
<div class="details-content">

预测数据，指定为Dataframe。X 的每一行对应一个观测值，每一列对应一个预测变量。最后一行为标签。

**数据类型:**  Dataframe

  </div>
</div>


### 名称-值对组参数

指定可选的、以逗号分隔的 Key=Value 对组参数。Key 为参数名称，Value 为对应的值。您可采用任意顺序指定多个名称-值对组参数，如 Key1=Value1,...,KeyN=ValueN 所示。

**示例：**


<div id="n_estimators" class="jump-target"></div>
<div class="details-box">
<details open>
<summary>n_estimators - 弱模型基数<div>12 （默认） | 数值</div></summary>
</details>
<div class="details-content">

对应弱模型的基数数量。

**数据类型:**  Int64

  </div>
</div>

<div id="max_depth" class="jump-target"></div>
<div class="details-box">
<details open>
<summary>max_depth - 模型最大深度<div>9 （默认） | 数值</div></summary>
</details>
<div class="details-content">

最大深度默认值为9

**数据类型:**  Int64

  </div>
</div>

<div id="min_samples_leaf" class="jump-target"></div>
<div class="details-box">
<details open>
<summary>min_samples_leaf - 模型最小枝叶<div>1 （默认） | 数值</div></summary>
</details>
<div class="details-content">

模型最小枝叶默认值为1

**数据类型:**  Int64

  </div>
</div>



## 输出参数

<div id="mdl" class="jump-target"></div>
<div class="details-box">
<details open>
<summary>mdl - 输出值<div>判别分析对象</div></summary>
</details>
<div class="details-content">

经过训练的判别分析分类模型，作为分类判别模型对象返回。

  </div>
</div>
