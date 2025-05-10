from src.controllers.score_controller import ScoreController
from src.controllers.user_controller import UserController
from src.services.score_service import ScoreService

# Score dependencies
score_service = ScoreService(None)
score_controller = ScoreController(score_service) # TODO: reemplazar con instancia de ScoreService

# User dependencies
user_controller = UserController(None) # TODO: reemplazar con instancia de UserService