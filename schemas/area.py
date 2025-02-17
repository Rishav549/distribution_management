class Area(BaseModel):
    area_name: str
    city: str
    state: str
    pin: str
    scode: str


class AreaCreate(Area):
    pass


class AreaView(Area):
    id: int