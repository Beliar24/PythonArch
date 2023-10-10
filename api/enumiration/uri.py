import enum
from dataclasses import dataclass


@dataclass
class Uri(enum.Enum):
    create_user = 'user'
    get_user = 'user/'
