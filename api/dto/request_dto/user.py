from dataclasses import dataclass, asdict


@dataclass
class User:
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int

    def to_dict(self):
        return asdict(self)
