import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, Base, engine

# Create the test client
client = TestClient(app)

# Use a fixture to set up and tear down the database before/after each test
@pytest.fixture(scope="module")
def setup_db():
    # Create the test database
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    yield db
    
    db.close()
    Base.metadata.drop_all(bind=engine)

def test_create_album_api(setup_db):
    response = client.post(
        "/api/albums/", json={"title": "Test Album", "artist": "Test Artist", "track_count": 10, "is_published": True}
    )
    
    assert response.status_code == 200
    assert response.json()["title"] == "Test Album"
    assert response.json()["artist"] == "Test Artist"
    assert response.json()["track_count"] == 10

def test_create_album_with_missing_field(setup_db):
    # Send a request with a missing required field like 'track_count'
    response = client.post(
        "/api/albums/", json={"title": "Incomplete Album", "artist": "Unknown Artist", "is_published": True}
    )

    assert response.status_code == 422  # FastAPI's default validation error, usually 422
    assert "track_count" in response.json()["detail"][0]["loc"]  # Ensure the error message is at the correct location


def test_get_album_api(setup_db):
    response = client.get("/api/albums/1")  # Assuming album with ID 1 exists
    assert response.status_code == 200

def test_read_non_existing_album_api(setup_db):
    # Send a request with a non-existing album_id
    response = client.get("/api/albums/99999")  # Assuming 99999 is not a valid album ID

    assert response.status_code == 404  # Should return a 404 Not Found error
    assert response.json() == {"detail": "Album not found"}  # FastAPI's standard error message


def test_update_album_api(setup_db):
    response = client.put(
        "/api/albums/1", json={"title": "Updated Album", "artist": "Updated Artist", "track_count": 12, "is_published": False}
    )
    
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Album"
    assert response.json()["artist"] == "Updated Artist"

def test_update_album_with_invalid_data(setup_db):
    # Send invalid data to update an existing album
    response = client.put(
        "/api/albums/1", json={"title": "Invalid Album", "artist": "Invalid Artist", "track_count": "fifteen", "is_published": "true"}
    )

    assert response.status_code == 422  # May return a 422 error due to invalid data
    assert "track_count" in response.json()["detail"][0]["loc"]  # Ensure the error message is at the correct location

def test_update_non_existing_album_api(setup_db):
    # Send a request to update a non-existing album ID
    response = client.put(
        "/api/albums/99999", json={"title": "Updated Title", "artist": "Updated Artist", "track_count": 15, "is_published": False}
    )

    assert response.status_code == 404  # Should return a 404 Not Found error
    assert response.json() == {"detail": "Album not found"}  # Error message


def test_delete_album_api(setup_db):
    response = client.delete("/api/albums/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Album deleted successfully"}


def test_delete_non_existing_album_api(setup_db):
    # Send a request to delete a non-existing album ID
    response = client.delete("/api/albums/99999")  # 99999 is a non-existing album ID

    assert response.status_code == 404  # Should return a 404 Not Found error
    assert response.json() == {"detail": "Album not found"}  # Error message
