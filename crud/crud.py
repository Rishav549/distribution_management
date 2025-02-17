from sqlalchemy.orm import Session
from sqlalchemy import desc
from models.employee_master import UserModel
from schemas.employee_master import Employee_create
from schemas.attendance import Attendance_create
from models.attendance import AttendanceModel
from schemas.monitor import Monitor_create
from models.monitor import MonitorModel
from models.device import DeviceModel
from schemas.device import Device_create
from schemas.area import AreaCreate
from models.area import Area

async def post_employee_details(db: Session, data: Employee_create):
    post_employee_details = UserModel(**data.dict())
    db.add(post_employee_details)
    db.commit()
    db.refresh(post_employee_details)
    return post_employee_details

async def get_employee(skip:int, limit: int, db: Session):
    return db.query(UserModel).offset(skip).limit(limit).all()

async def post_attendance(db:Session, data: Attendance_create):
    post_attendance = AttendanceModel(**data.dict())
    db.add(post_attendance)
    db.commit()
    db.refresh(post_attendance)
    return post_attendance

async def get_attendance(skip:int, limit: int, db: Session):
    return db.query(AttendanceModel).offset(skip).limit(limit).all()

async def post_monitor(db:Session, data: Monitor_create):
    post_monitor = MonitorModel(**data.dict())
    db.add(post_monitor)
    db.commit()
    db.refresh(post_monitor)
    return post_monitor

async def get_monitor(skip:int, limit: int, db: Session):
    return db.query(MonitorModel).offset(skip).limit(limit).all()

async def post_device(db:Session, data:Device_create):
    device = DeviceModel(**data.dict())
    db.add(device)
    db.commit()
    db.refresh(device)
    return device

async def get_device(skip: int, limit:int, db: Session, scan_code: str | None = None):
    query=db.query(DeviceModel)
    if scan_code:
        query=query.filter(DeviceModel.scan_code == scan_code)
    return query.offset(skip).limit(limit).all()

async def post_area(db:Session, data: AreaCreate):
    area= Area(**data.dict())
    db.add(area)
    db.commit()
    db.refresh(area)
    return area

async def get_area(skip: int, limit: int, db: Session, area_name: str | None = None):
    query = db.query(Area)
    if area_name:
        query = query.filter(Area.area_name == area_name)
    return query.offset(skip).limit(limit).all()

