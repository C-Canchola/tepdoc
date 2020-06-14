import click
import os

import tepdoc.api.render as render

@click.group()
@click.argument('root_path', help="Root path of directory to document.")
@click.pass_context
def cli(ctx, root_path: str):
    """
    Root command for tepdoc cli

    Args:
        ctx ():
        root_path ():

    Returns:

    """
    ctx.obj['ROOT_PATH'] = root_path


@cli.command()
def init(ctx):
    """
    Initializes asset directory with json data for documentation html.
    Returns:

    """

    click.echo(os.getcwd())
