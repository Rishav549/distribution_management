from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import get_db
from fastapi.responses import JSONResponse
from schemas.location_type import LocationTypeCreate
from crud.crud import post_location_type, get_location_types

router = APIRouter()

@router.post("/location_type/")
async def create_location_type(data: LocationTypeCreate, db: Session = Depends(get_db)):
    try:
        result = await post_location_type(db=db, data=data)
        return result
    except HTTPException as e:
        return JSONResponse(content={"detail": e.detail}, status_code=e.status_code)

@router.get("/location_type/get")
async def fetch_location_types(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    location_types = await get_location_types(db=db, skip=skip, limit=limit)
    return location_types
