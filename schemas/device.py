from pydantic import BaseModel

class Device(BaseModel):
    scan_code: str
    mac_id: str

class Device_create(Device):
    pass

class Device_view(Device):
    id: int