from db.db import Base
from sqlalchemy import ForeignKey, Integer,String,Column,DateTime,Boolean
import datetime

class LocationTag(Base):
    __tablename__ = "location_tag"

    id = Column(Integer, primary_key=True, index=True)
    location_code = Column(String, nullable=False, unique=True)
    location_name = Column(String, nullable=False)
    location_type = Column(String, nullable=False)
    address = Column(String, nullable=False)
    location = Column(String, nullable=False)
    city = Column(String, nullable=False)
    pin = Column(String, nullable=False)
    lat = Column(String, nullable=False)
    lan = Column(String, nullable=False)
    entry_by_emp_id = Column(Integer, ForeignKey("employee_master.id"),  nullable=False)
    date_of_entry = Column(String, nullable=False)
    area_code = Column(Integer, ForeignKey("area.area_id"), nullable=False)
    image = Column(String, nullable=False)
    contact_person = Column(String, nullable=False)
    contact_no = Column(String, nullable=False)
