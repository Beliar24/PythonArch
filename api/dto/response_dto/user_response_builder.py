from dataclasses import dataclass


@dataclass
class UserResponseBuilder:

    code: int
    type: str
    message: str

    def to_dict(self):
        return {
            'code': self.code,
            'type': self.type,
            'message': self.message
        }
