from dataclasses import dataclass


@dataclass
class GetUserResponseBuilder:
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int
