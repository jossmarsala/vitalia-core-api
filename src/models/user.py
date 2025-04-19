# Clase User

class UserModel:
    def __init__(self, username: str, password: str, data: dict):
        self.username: str = username
        self.password: str = password
        self.data: dict = data

    def to_json(self):
        return self.__dict__