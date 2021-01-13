from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.advert import create_random_advert


def test_create_advert(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {"title": "Foo", "description": "Fighters"}
    response = client.post(
        f"{settings.API_V1_STR}/adverts/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert content["location"] == data["location"]
    assert content["is_active"] == data["is_active"]
    assert "id" in content
    assert "owner_id" in content


def test_read_advert(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    advert = create_random_advert(db)
    response = client.get(
        f"{settings.API_V1_STR}/adverts/{advert.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == advert.title
    assert content["description"] == advert.description
    assert content["location"] == advert.location
    assert content["is_active"] == advert.is_active
    assert content["id"] == advert.id
    assert content["owner_id"] == advert.owner_id
