from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Advert])
def read_adverts(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve adverts.
    """
    if crud.user.is_superuser(current_user):
        adverts = crud.advert.get_multi(db, skip=skip, limit=limit)
    else:
        adverts = crud.advert.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return adverts


@router.post("/", response_model=schemas.Advert)
def create_advert(
    *,
    db: Session = Depends(deps.get_db),
    advert_in: schemas.AdvertCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new advert.
    """
    advert = crud.advert.create_with_owner(db=db, obj_in=advert_in, owner_id=current_user.id)
    return advert


@router.put("/{id}", response_model=schemas.Advert)
def update_advert(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    advert_in: schemas.AdvertUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an advert.
    """
    advert = crud.advert.get(db=db, id=id)
    if not advert:
        raise HTTPException(status_code=404, detail="Advert not found")
    if not (advert.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    advert = crud.advert.update(db=db, db_obj=advert, obj_in=advert_in)
    return advert


@router.get("/{id}", response_model=schemas.Advert)
def read_advert(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get advert by ID.
    """
    advert = crud.advert.get(db=db, id=id)
    if not advert:
        raise HTTPException(status_code=404, detail="Advert not found")
    return advert


@router.delete("/{id}", response_model=schemas.Advert)
def delete_advert(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an advert.
    """
    advert = crud.advert.get(db=db, id=id)
    if not advert:
        raise HTTPException(status_code=404, detail="Advert not found")
    if not (advert.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    advert = crud.advert.remove(db=db, id=id)
    return advert
