from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from db.db import get_db
from schemas.location_tag import LocationTagCreate
from crud.crud import post_location_tag, get_location_tags
import uuid
import os

router = APIRouter()

UPLOAD_DIRECTORY = "./uploaded_images/location_tags"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@router.post("/location_tag/")
async def create_location_tag(
    location_code: str = Form(...),
    location_name: str = Form(...),
    location_type: int = Form(...),
    address: str = Form(...),
    location: str = Form(...),
    city: str = Form(...),
    pin: str = Form(...),
    lat: str = Form(...),
    lan: str = Form(...),
    entry_by_emp_id: int = Form(...),
    date_of_entry: str = Form(...),
    area_code: int = Form(...),
    contact_person: str = Form(...),
    contact_no: str = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)):
    try:
        unique_filename = f"{uuid.uuid4()}.png"
        image_path = os.path.join(UPLOAD_DIRECTORY, unique_filename)
        
        with open(image_path, "wb") as buffer:
            buffer.write(await image.read())

        location_tag_data = {
            "location_code": location_code,
            "location_name": location_name,
            "location_type": location_type,
            "address": address,
            "location": location,
            "city": city,
            "pin": pin,
            "lat": lat,
            "lan": lan,
            "entry_by_emp_id": entry_by_emp_id,
            "date_of_entry": date_of_entry,
            "area_code": area_code,
            "contact_person": contact_person,
            "contact_no": contact_no,
            "image": image_path
        }

        result = await post_location_tag(db=db, data=location_tag_data)
        return result
    except HTTPException as e:
        return JSONResponse(content={"detail": e.detail}, status_code=e.status_code)

@router.get("/location_tag/get")
async def fetch_location_tags(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), area_code: str =None):
    location_tags = await get_location_tags(db=db, skip=skip, limit=limit, area_code=area_code)
    return location_tags
