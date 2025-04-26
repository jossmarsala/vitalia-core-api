from abc import ABC, abstractmethod

class AbstractUser(ABC):
    def __init__(self, username: str, password: str, data: dict):
        self.username = username
        self.password = password
        self.data = data

    @abstractmethod
    def to_dict(self) -> dict:
        pass
