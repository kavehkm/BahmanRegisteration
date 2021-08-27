# standard
import hashlib


def check(license_file, settings_file, salt):
    # read license
    with open(license_file, 'rt') as f:
        lisense = f.read().strip()
    # read settings file content
    with open(settings_file, 'rt', encoding='utf-8') as f:
        content = ''
        for line in f.readlines()[1:]:
            content += line.strip()
    # append salt to settings content
    content += salt
    # check for license
    return hashlib.md5(content.encode()).hexdigest() == lisense
