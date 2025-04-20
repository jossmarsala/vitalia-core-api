class UserModel:
    def __init__(self, username: str, password: str, data: dict):
        self.username = username
        self.password = password
        self.data = data

    def to_dict(self):
        return self.__dict__