from src.controllers.score_controller import ScoreController
from src.controllers.user_controller import UserController
from src.services.score_service import ScoreService

# Score dependencies
score_service = ScoreService()
score_controller = ScoreController(score_service)

# User dependencies
user_controller = UserController(None)