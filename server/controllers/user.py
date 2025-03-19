from fastapi import APIRouter

router = APIRouter(prefix="/user")


@router.get("/login")
async def login():
    return {"message": "Login"}
