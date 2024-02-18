import configparser
import os

from api.utils.settings import current_location


def get_users_config(section, option):
    config = configparser.ConfigParser()
    config.read(current_location("endpoints") + 'users.ini')
    return config.get(section, option)
