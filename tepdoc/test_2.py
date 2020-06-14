import jinja2 as jn
from tepdoc.api.doc_objs import DocRoot
import os

if __name__ == '__main__':
    with open('templates/doc_template.html', 'r') as f:
        template_str = f.read()

    tmp = jn.Template(template_str)

    doc_root = DocRoot(os.path.abspath('test_root'))
    doc_root.write_to_json()
    str = tmp.render(doc_root=doc_root)

    with open('README.html', 'w') as f:
        f.write(str)
