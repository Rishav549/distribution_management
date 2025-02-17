from pydantic import BaseModel
from datetime import datetime

class LocationTypeBase(BaseModel):
    location_type: str
    scode: str
    loc_icon: str

class LocationTypeCreate(LocationTypeBase):
    pass

class LocationTypeView(LocationTypeBase):
    id: int
