from sqlalchemy import Column, String

from app.shared.db.base import Base, generate_uuid


class Dealer(Base):
    __tablename__ = "dealers"
    __table_args__ = {"schema": "auth"}

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False, default="dealer")
