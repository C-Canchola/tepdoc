import os
import json

from tepdoc.api.assets import get_mk_asset_dir_path

ROOT_READ_JSON = os.path.join(get_mk_asset_dir_path(), 'root_read.json')

ROOT_INFO_DEFAULT = 'Enter information about the root directory.'
SUBDIR_INFO_DEFAULT = 'Enter information about subdirectory'


def get_json_dict():
    if not os.path.exists(ROOT_READ_JSON):
        return {}
    with open(ROOT_READ_JSON, 'r') as f:
        return json.loads(f.read())


class DocRoot:

    def __init__(self, path: str):
        self._json_dict = get_json_dict()
        self.path = path
        self.name = os.path.split(self.path)[-1]

    @property
    def info(self):
        return self._json_dict.get('info', ROOT_INFO_DEFAULT)

    @property
    def json_dict(self):
        return self._json_dict

    @property
    def sub_dirs(self):
        items = [item for item in os.listdir(self.path)]
        item_paths = [os.path.join(self.path, item) for item in items]
        dir_nms = [os.path.split(item)[-1] for item in item_paths if os.path.isdir(item)]
        return [DocSubDir(self, dir_nm) for dir_nm in dir_nms]

    def sub_dir_dict(self):
        return {sub_dir.ino: sub_dir.to_dict() for sub_dir in self.sub_dirs}

    def to_dict(self):
        return {'name': self.name, 'info': self.info, 'sub_dirs': self.sub_dir_dict()}

    def write_to_json(self):
        with open(ROOT_READ_JSON, 'w') as f:
            f.write(json.dumps(self.to_dict(), indent=4))

    def get_subdir_dict(self, sub_dir):
        all_subdir_dict = self._json_dict.get("sub_dirs", {})
        return all_subdir_dict.get(str(sub_dir.ino), {})


class DocSubDir:

    def __init__(self, root: DocRoot, nm: str):
        self.name = nm
        self.path = os.path.join(root.path, nm)
        self.root = root
        self.ino = os.stat(self.path).st_ino
        self.info_dict = self.root.get_subdir_dict(self)

    @property
    def info(self):
        return self.info_dict.get('info', SUBDIR_INFO_DEFAULT)

    @property
    def files(self):
        item_paths = [os.path.join(self.path, item) for item in os.listdir(self.path)]
        file_nms = [os.path.split(item)[-1] for item in item_paths if os.path.isfile(item)]
        return [DocFile(self, file_nm) for file_nm in file_nms]

    def to_dict(self):
        return {'name': self.name, 'info': self.info, 'ino': self.ino}


class DocFile:

    def __init__(self, sub_dir: DocSubDir, nm: str):
        self.name = nm
        self.path = os.path.join(sub_dir.path, self.name)
