from pydantic import BaseModel
from sqlalchemy.sql import false


class VehicleCreate(BaseModel):
    id: str
    dealer_id: str
    vin: str
    plate: str
    brand: str
    model: str
    year: int
    color: str


class VehicleResponse(BaseModel):
    id: str
    dealer_id: str
    vin: str
    plate: str
    brand: str
    model: str
    year: int
    color: str

    class Config:
        from_attributes = True
