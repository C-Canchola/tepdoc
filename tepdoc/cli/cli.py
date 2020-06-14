import click
import os

from functools import wraps

import tepdoc.api.assets as assets
import tepdoc.api.render as rdr

from tepdoc.api.doc_objs import DocRoot


def validate_root_path(root_path: str):
    concat_path = os.path.join(os.getcwd(), root_path)
    if not os.path.exists(concat_path):
        raise ValueError('Error: {} does not exist'.format(concat_path))
    if not os.path.isdir(concat_path):
        raise ValueError('Error: {} is not a directory path'.format(concat_path))


@click.group()
@click.argument('root_path')
@click.pass_context
def cli(ctx, root_path):
    """
    Root command for tepdoc cli

    """

    validate_root_path(root_path)

    ctx.ensure_object(dict)
    ctx.obj['ROOT_PATH'] = root_path


@cli.command()
@click.option('--edit/--no-edit', '-e', default=False, help='Edit flag to open read json in text editor.')
@click.pass_context
def init(ctx, edit):
    """
    Initializes asset directory with json data for documentation html.

    """
    assets.initialize_asset_dir()
    rdr.initialize_doc(ctx.obj['ROOT_PATH'])

    if edit:
        click.launch(assets.get_root_read_json_path())


@cli.command()
def edit():
    """
    Opens the json data file for editing with default text editor.
    Returns:

    """
    click.launch(assets.get_root_read_json_path())


@cli.command()
@click.option('--open/--no-open', '-o/-n', default=True,
              help='Open flag that determines whether the rendered html will be displayed.')
@click.pass_context
def render(ctx, open):
    """
    Renders the documentation html for a root path containing directories with files to be documented.
    Returns:

    """

    rdr.render_template(ctx.obj['ROOT_PATH'])

    if open:
        click.launch(rdr.DOC_PATH)
