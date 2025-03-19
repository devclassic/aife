from fastapi import APIRouter, Request
from models.user import User
from uuid import uuid4

router = APIRouter(prefix="/auth")


# 管理员登录接口
# 参数 username, password
@router.post("/admin_login")
async def login(request: Request):
    data = await request.json()
    user = await User.get_or_none(
        username=data.get("username"), password=data.get("password"), is_admin=True
    )
    if not user:
        return {"success": False, "message": "用户名或密码错误"}
    else:
        token = uuid4()
        user.token = str(token)
        await user.save(update_fields=["token"])
        return {"success": True, "message": "登录成功", "token": token}
