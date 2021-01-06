import uuid
from typing import Optional

from pydantic import BaseModel


# Shared properties
class AdvertBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    is_active: Optional[bool] = None


# Properties to receive on Advert creation
class AdvertCreate(AdvertBase):
    title: str
    description: str
    location: str
    is_active: bool

# Properties to receive on Advert update
class AdvertUpdate(AdvertBase):
    title: str
    description: str
    is_active: bool


# Properties shared by models stored in DB
class AdvertInDBBase(AdvertBase):
    id: uuid.UUID
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Advert(AdvertInDBBase):
    pass


# Properties properties stored in DB
class AdvertInDB(AdvertInDBBase):
    pass
