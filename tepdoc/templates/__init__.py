import jinja2 as jn
import os

DIR_PATH = os.path.dirname(__file__)
TEMPLATE_PATH = os.path.join(DIR_PATH, 'doc_template.html')


def get_doc_template() -> jn.Template:
    with open(TEMPLATE_PATH, 'r') as f:
        template_str = f.read()

    return jn.Template(template_str)
