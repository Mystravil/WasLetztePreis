from typing import TYPE_CHECKING
import uuid
import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .advert import Advert # noqa: F401


class User(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    full_name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(Integer, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    adverts = relationship("Advert", back_populates="owner")
    created_date = Column(DateTime(), nullable=False, default=datetime.datetime.utcnow())
    updated_date = Column(DateTime(), nullable=False, default=datetime.datetime.utcnow())
