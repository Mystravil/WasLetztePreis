from typing import Optional

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.advert import AdvertCreate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def create_random_advert(db: Session, *, owner_id: Optional[int] = None) -> models.Advert:
    if owner_id is None:
        user = create_random_user(db)
        owner_id = user.id
    title = random_lower_string()
    description = random_lower_string()
    location = random_lower_string()
    is_active = True
    advert_in = AdvertCreate(title=title, description=description, location=location, is_active=is_active, id=id)
    return crud.advert.create_with_owner(db=db, obj_in=advert_in, owner_id=owner_id)
