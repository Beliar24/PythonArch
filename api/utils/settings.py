import os


def current_location(directory):
    current_path = os.path.abspath(__file__)
    api_path = os.path.dirname(os.path.dirname(current_path))
    return os.path.join(api_path, f'{directory}\\')
