from .home import router as home_router
from .auth import router as auth_router
from .user import router as user_router
from .app import router as app_router
from .account import router as account_router

routers = [auth_router, home_router, user_router, app_router, account_router]
