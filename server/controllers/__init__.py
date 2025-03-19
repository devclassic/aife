from .home import router as home_router
from .auth import router as auth_router
from .user import router as user_router

routers = [auth_router, home_router, user_router]
