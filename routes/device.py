from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import get_db
from fastapi.responses import JSONResponse
from datetime import datetime
from schemas.device import Device_create,Device_view
from crud.crud import post_device, get_device

router = APIRouter()

@router.post("/device")
async def create_device(data: Device_create, db: Session=Depends(get_db)):
    try:
        result = await post_device(db=db, data=data)
        return result
    except HTTPException as e:
        print(e)
        return JSONResponse(content={"detail": e.detail}, status_code=e.status_code)

@router.get("/device/get")
async def get_data(skip: int= 0, limit: int =10, db: Session =Depends(get_db), scan_code: str = None):
    get_data = await get_device(db=db, skip=skip, limit=limit, scan_code=scan_code)
    return get_data