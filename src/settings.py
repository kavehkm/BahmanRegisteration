# standard
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SETTINGS_FILE_PATH = os.path.join(BASE_DIR, 'settings.txt')


class Settings(object):
    """Settings Class"""
    def __init__(self):
        self._dict = dict()
        self._load_file()

    def _load_file(self):
        with open(SETTINGS_FILE_PATH, 'rt') as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            key, value = line.split('=')
            setattr(self, key, value)
            self._dict[key] = value

    def as_dict(self):
        return self._dict
