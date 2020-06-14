"""
module for initializing tepdoc-assets in a directory.
"""
import os
import shutil

API_DIR = os.path.split(__file__)[-1]
PROJECT_DIR = os.path.split(API_DIR)[-1]
ASSET_DIR = os.path.join(PROJECT_DIR, 'pkg_assets')


def get_asset_paths() -> list:
    return [os.path.join(ASSET_DIR, f) for f in os.listdir(ASSET_DIR)]


def get_mk_asset_dir_path():
    return os.path.join(os.getcwd(), 'tepdoc-assets')


def create_asset_dir():
    try:
        os.mkdir(get_mk_asset_dir_path())
    except:
        pass

def initialize_asset_dir():
    create_asset_dir()
    asset_mk_path = get_mk_asset_dir_path()
    for asset_path in get_asset_paths():
        shutil.move(asset_path, asset_mk_path)

