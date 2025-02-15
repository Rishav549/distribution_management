from db.db import Base
from sqlalchemy import ForeignKey, Integer,String,Column,DateTime,Boolean
import datetime

class DeviceModel(Base):
    __tablename__="device"
    id = Column(Integer, primary_key=True, autoincrement=True)
    scan_code = Column(String, nullable=False)
    mac_id = Column(String, nullable=False)