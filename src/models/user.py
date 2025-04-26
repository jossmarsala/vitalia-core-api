from .abstract_user import AbstractUser

class UserModel(AbstractUser):
    def __init__(self, username: str, password: str, data: dict):
        super().__init__(username, password, data)

    def to_dict(self):
        return self.__dict__
