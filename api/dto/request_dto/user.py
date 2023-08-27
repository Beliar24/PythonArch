class User:
    def __init__(self, user_id, username, firstName, lastName, email, password, phone, userStatus):
        self.id = user_id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = userStatus

    @staticmethod
    def get_dto_dict(user_id, username, firstName, lastName, email, password, phone, userStatus):
        return User(user_id, username, firstName, lastName, email, password, phone, userStatus).__dict__
