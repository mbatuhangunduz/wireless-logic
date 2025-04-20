from pydantic import BaseModel
from typing import Optional

# Base model for Album
class AlbumBase(BaseModel):
    title: str 
    is_published: bool = True
    track_count: int 
    artist: str
    # release_year = int

class AlbumCreate(AlbumBase):
    pass  

class Album(AlbumBase):
    id: int  

    class Config:
        orm_mode = True  
