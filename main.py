import yaml
from jinja2 import Template

config_name = "template"
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