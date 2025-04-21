from pydantic import BaseModel
from typing import Optional

# Base model for Album
class AlbumBase(BaseModel):
    title: str 
    is_published: bool = True
    track_count: int 
    artist: str
    publish_year: Optional[int] = None
    detail: Optional[str] = None
    is_single: Optional[bool] = False
    number_of_stream: Optional[int] = None
    deneme_m : Optional[str] = None
    deneme_k : Optional[str] = None

class AlbumCreate(AlbumBase):
    pass  

class Album(AlbumBase):
    id: int  

    class Config:
        orm_mode = True  
