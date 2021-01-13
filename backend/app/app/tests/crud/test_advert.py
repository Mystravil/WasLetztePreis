from sqlalchemy.orm import Session

from app import crud
from app.schemas.advert import AdvertCreate, AdvertUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def test_create_advert(db: Session) -> None:
    advert_in = this.generate_random_advert()
    user = create_random_user(db)
    advert = crud.advert.create_with_owner(db=db, obj_in=advert_in, owner_id=user.id)
    assert advert.title == title
    assert advert.description == description
    assert advert.owner_id == user.id


def test_get_advert(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    advert_in = AdvertCreate(title=title, description=description)
    user = create_random_user(db)
    advert = crud.advert.create_with_owner(db=db, obj_in=advert_in, owner_id=user.id)
    stored_advert = crud.advert.get(db=db, id=advert.id)
    assert stored_advert
    assert advert.id == stored_advert.id
    assert advert.title == stored_advert.title
    assert advert.description == stored_advert.description
    assert advert.owner_id == stored_advert.owner_id


def test_update_advert(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    advert_in = AdvertCreate(title=title, description=description)
    user = create_random_user(db)
    advert = crud.advert.create_with_owner(db=db, obj_in=advert_in, owner_id=user.id)
    description2 = random_lower_string()
    advert_update = AdvertUpdate(description=description2)
    advert2 = crud.advert.update(db=db, db_obj=advert, obj_in=advert_update)
    assert advert.id == advert2.id
    assert advert.title == advert2.title
    assert advert2.description == description2
    assert advert.owner_id == advert2.owner_id


def test_delete_advert(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    advert_in = AdvertCreate(title=title, description=description)
    user = create_random_user(db)
    advert = crud.advert.create_with_owner(db=db, obj_in=advert_in, owner_id=user.id)
    advert2 = crud.advert.remove(db=db, id=advert.id)
    advert3 = crud.advert.get(db=db, id=advert.id)
    assert advert3 is None
    assert advert2.id == advert.id
    assert advert2.title == title
    assert advert2.description == description
    assert advert2.owner_id == user.id

def generate_random_advert():
    title = random_lower_string()
    description = random_lower_string()
    location = random_lower_string()
    is_active = True
    return AdvertCreate(title=title, description=description, location=location, is_active=is_active)
