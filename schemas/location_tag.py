class LocationTag(BaseModel):
    location_code: str
    location_name: str
    location_type: str
    address: str
    location: str
    city: str
    pin: str
    lat: str
    lan: str
    entry_by_emp_id: str
    date_of_entry: str
    area_code: str
    image: str
    contact_person: str
    contact_no: str


class LocationTagCreate(LocationTag):
    pass


class LocationTagView(LocationTag):
    id: int