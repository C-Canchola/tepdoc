import jinja2 as jn

def get_doc_template() -> jn.Template:
    with open('doc_template.html', 'r') as f:
        template_str = f.read()

    return jn.Template(template_str)
