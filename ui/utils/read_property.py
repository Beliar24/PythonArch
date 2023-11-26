import os

from jproperties import Properties


def get_property(name):
    configs = Properties()

    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, 'ui.properties')

    with open(file_path, 'rb') as config_file:
        configs.load(config_file)

    return configs.get(name).data
