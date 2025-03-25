from fastapi import APIRouter, Request, Depends
from fastapi_pagination import Params
from fastapi_pagination.ext.tortoise import paginate
from models import History
from dtos.common import DataList, HistoryPydantic

router = APIRouter(prefix="/history")


@router.post("/remove")
async def remove(request: Request):
    data = await request.json()
    history = await History.get_or_none(id=data["id"])
    if not history:
        return {"success": False, "message": "应用不存在"}
    await history.delete()
    return {"success": True, "message": "删除成功"}


@router.post("/remove_batch")
async def remove_batch(request: Request):
    data = await request.json()
    await History.filter(id__in=data["ids"]).delete()
    return {"success": True, "message": "删除成功"}


@router.post("/get")
async def get(request: Request):
    data = await request.json()
    history = await History.get_or_none(id=data["id"]).select_related("account", "app")
    if not history:
        return {"success": False, "message": "应用不存在"}
    return {"success": True, "message": "获取成功", "data": history}


@router.post("/list", response_model=DataList[HistoryPydantic])
async def list(params: Params = Depends()):
    historys = await paginate(
        History.all().select_related("account", "app").order_by("-id"), params
    )
    result = DataList[HistoryPydantic](success=True, message="获取成功", data=historys)
    return result
