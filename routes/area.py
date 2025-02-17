from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import get_db
from fastapi.responses import JSONResponse
from schemas.area import AreaCreate, AreaView
from crud.crud import post_area, get_area

router = APIRouter()

@router.post("/area/")
async def post_area_route(data: AreaCreate, db: Session = Depends(get_db)):
    try:
        result = await post_area(db=db, data=data)
        return result
    except HTTPException as e:
        print(e)
        return JSONResponse(content={"detail": e.detail}, status_code=e.status_code)

@router.get("/area/get")
async def get_area_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), area_name: str = None):
    try:
        result = await get_area(db=db, skip=skip, limit=limit, area_name=area_name)
        return result
    except HTTPException as e:
        print(e)
        return JSONResponse(content={"detail": e.detail}, status_code=e.status_code)
