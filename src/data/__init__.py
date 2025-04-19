from typing import List
from .db import initialize_data
from src.models.user import UserModel

db: List[UserModel] = initialize_data()