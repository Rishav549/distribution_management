from db.db import Base
from sqlalchemy import ForeignKey, Integer,String,Column,DateTime,Boolean

class LocationType(Base):
    __tablename__="location_type"

    id = Column(Integer, primary_key=True, index=True)
    location_type = Column(String, nullable=False)
    scode = Column(String, nullable=False)
    loc_icon=Column(String, nullable=True)