from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.obd2.schemas import ScanCreate
from app.shared.db.session import get_db
from app.vehicles.repository import VehicleRepository
from app.vehicles.schemas import VehicleCreate, VehicleResponse

router = APIRouter(prefix="/vehicles", tags=["vehicles"])


@router.get("/vehicles/{vehicle_id}", response_model=VehicleResponse)
def get_vehicle_by_id(vehicle_id: str, db: Session = Depends(get_db)):
    repo = VehicleRepository(db)
    return repo.get_vehicle_by_id(vehicle_id)


@router.post("/vehicles", response_model=ScanCreate)
def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    repo = VehicleRepository(db)
    new_vehicle = repo.create_vehicle(
        vin=vehicle.vin,
        plate=vehicle.plate,
        brand=vehicle.brand,
        model=vehicle.model,
        year=vehicle.year,
        color=vehicle.color,
    )

    return new_vehicle
