"""
Rendering and editing of the json for the generated html.
"""
import os

from tepdoc.templates import get_doc_template
from tepdoc.api.doc_objs import DocRoot

DOC_TEMPLATE = get_doc_template()
DOC_NAME = 'README.html'
DOC_PATH = os.path.join(os.getcwd(), DOC_NAME)


def get_doc_path():
    os.path.join(os.getcwd(), DOC_NAME)


def initialize_doc(root_path: str):
    get_doc_root(root_path).write_to_json()


def get_doc_root(root_path: str) -> DocRoot:
    root_path = os.path.abspath(root_path)
    return DocRoot(root_path)


def render_template(root_path: str):
    with open(DOC_PATH, 'w') as f:
        f.write(DOC_TEMPLATE.render(doc_root=get_doc_root(root_path)))
