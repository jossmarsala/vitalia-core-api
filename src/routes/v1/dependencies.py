from src.controllers.score_controller import ScoreController
from src.controllers.user_controller import UserController
from src.services.score_service import ScoreService
from src.services.user_service import UserService

# Score dependencies
score_service = ScoreService()
score_controller = ScoreController(score_service)

# User dependencies
user_service = UserService()
user_controller = UserController(user_service)