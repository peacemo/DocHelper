import os
import argparse
import yaml
from jinja2 import Template

parser = argparse.ArgumentParser()
parser.add_argument("file_name", type=str, default="example", nargs="?",
                    help="The target YMAL FILE NAME to produce documentation. (default: example ymal file)")
args = parser.parse_args()

print(f"需要处理的文件为: {args.file_name}")
config_name = args.file_name

if os.path.exists(f"./outputs/{config_name}.md"):
    go_on = input(f"文件: ./outputs/{config_name}.md 已存在，继续执行将覆盖此文件[y/n]: ")
    if go_on.lower() == "y" or  go_on.lower() == "yes":
        pass
    else: 
        print("操作取消，程序退出。")
        exit()

# Load and parse the YAML file
with open(f"./configs/{config_name}.yml") as f:
    data = yaml.safe_load(f)

# Load and render the template file
with open("./template_doc.md") as f:
    template = Template(f.read())
    output = template.render(data)

# Write the output to a Markdown file
with open(f"./outputs/{config_name}.md", "w") as f:
    f.write(output)
