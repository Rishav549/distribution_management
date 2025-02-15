from db.db import Base
from sqlalchemy import ForeignKey, Integer,String,Column,DateTime,Boolean

class Area(Base):
    __tablename__ = "area"

    area_id = Column(Integer, primary_key=True, index=True)
    area_name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    pin = Column(String, nullable=False)
    scode = Column(String, nullable=False)