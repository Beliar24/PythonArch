from dataclasses import dataclass, asdict


@dataclass
class UserResponseBuilder:

    code: int
    type: str
    message: str

    def to_dict(self):
        return asdict(self)
