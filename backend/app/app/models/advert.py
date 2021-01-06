from typing import TYPE_CHECKING
import uuid
import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Advert(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    location = Column(String, index=True, nullable=False)
    is_active = Column(Boolean(), default=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    owner = relationship("User", back_populates="items")
    created_date = Column(DateTime(), nullable=False, default=datetime.datetime.utcnow())
    updated_date = Column(DateTime(), nullable=False, default=datetime.datetime.utcnow())
