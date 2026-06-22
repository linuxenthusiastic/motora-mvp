from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import foreign, relationship
from sqlalchemy.sql.expression import null, true
from sqlalchemy.sql.sqltypes import TIMESTAMP, Float

from app.shared.db.base import Base, generate_uuid


class OBD2Scan(Base):
    __tablename__ = "obd2_scan"
    __table_args__ = {"schema": "obd2"}

    id = Column(String, primary_key=True, default=generate_uuid)
    vehicle_id = Column(String, ForeignKey("obd2.vehicles.id"), nullable=False)
    scan_date = Column(TIMESTAMP, nullable=False)
    odometer = Column(Integer, nullable=False)
    rpm = Column(Integer, nullable=False)
    coolant_temp = Column(Float, nullable=False)
    battery_voltage = Column(Float, nullable=False)
    error_codes = Column(String, nullable=False)
    vehicle = relationship("Vehicle", back_populates="scans")
