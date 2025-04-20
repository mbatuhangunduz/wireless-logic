from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

router = APIRouter()

@router.get("/geldi")
def ping():
    return {"message": "gittimi"}

# Create a new album
@router.post("/albums/", response_model=schemas.Album)
async def create_album(album: schemas.AlbumCreate, db: Session = Depends(database.get_db)):
    return crud.create_album(db=db, album=album)


# Read a list of albums with pagination
@router.get("/albums/", response_model=list[schemas.Album])
async def get_all_albums(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    albums = crud.get_albums(db, skip=skip, limit=limit)
    return albums


# Read a specific album by its ID
@router.get("/albums/{album_id}", response_model=schemas.Album)
async def read_album(album_id: int, db: Session = Depends(database.get_db)):
    db_album = crud.get_album(db, album_id=album_id)
    if db_album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return db_album


# Update an existing album by its ID
@router.put("/albums/{album_id}", response_model=schemas.Album)
async def update_album(album_id: int, updated_data: schemas.AlbumCreate, db: Session = Depends(database.get_db)):
    album = crud.update_album(db, album_id, updated_data)
    if album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return album


# Delete an album by its ID
@router.delete("/albums/{album_id}", response_model=dict)
async def delete_album(album_id: int, db: Session = Depends(database.get_db)):
    album = crud.delete_album(db, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return {"message": "Album deleted successfully"}
