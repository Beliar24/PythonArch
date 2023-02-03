from jproperties import Properties


def get_property(name):
    configs = Properties()

    with open('D:\\Project\\pythonProject\\ui.properties', 'rb') as config_file:
        configs.load(config_file)

    return configs.get(name).data
