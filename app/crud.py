import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from . import models, schemas
from pydantic import validator

# Set up logging
logger = logging.getLogger(__name__)

# Get a specific album by its ID
def get_album(db: Session, album_id: int):
    try:
        return db.query(models.Album).filter(models.Album.id == album_id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving album with ID {album_id}: {e}")
        raise ValueError(f"Error retrieving album with ID {album_id}: {e}")

# Get a list of albums with pagination (skip and limit)
def get_albums(db: Session, skip: int = 0, limit: int = 10, sort_by: str = "id"):
    try:
        return db.query(models.Album).order_by(getattr(models.Album, sort_by)).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving albums with skip={skip}, limit={limit}: {e}")
        raise ValueError(f"Error retrieving albums: {e}")
    


# Create a new album
def create_album(db: Session, album: schemas.AlbumCreate):
    try:
        db_album = models.Album(
            title=album.title,
            is_published=album.is_published,
            artist=album.artist,
            track_count=album.track_count,
            publish_year=album.publish_year,
            detail=album.detail,
            is_single=album.is_single,
        )
        db.add(db_album)
        db.commit()
        db.refresh(db_album)
        logger.info(f"Album '{album.title}' created successfully.")
        return db_album
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error creating album '{album.title}': {e}")
        raise ValueError(f"Error creating album '{album.title}': {e}")

# Update an existing album
def update_album(db: Session, album_id: int, updated_data: schemas.AlbumCreate):
    try:
        album = get_album(db, album_id)
        if album:
            # Only update valid fields
            for key, value in updated_data.model_dump().items():
                if value is not None:  # Skip None values
                    setattr(album, key, value)
            db.commit()
            db.refresh(album)
            logger.info(f"Album with ID {album_id} updated successfully.")
            return album
        else:
            logger.error(f"Album with ID {album_id} not found.")
            return None
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error updating album with ID {album_id}: {e}")
        raise ValueError(f"Error updating album with ID {album_id}: {e}")

# Delete an album by ID
def delete_album(db: Session, album_id: int):
    try:
        album = get_album(db, album_id)
        if album:
            db.delete(album)
            db.commit()
            logger.info(f"Album with ID {album_id} deleted successfully.")
            return True  # Album deleted successfully
        else:
            logger.warning(f"Album with ID {album_id} not found.")
            return False  # Album not found
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error deleting album with ID {album_id}: {e}")
        raise ValueError(f"Error deleting album with ID {album_id}: {e}")