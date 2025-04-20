from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

# Album Model
class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False, index=True) 
    is_published = Column(Boolean, default=True) 
    track_count = Column(Integer, nullable=False)  # Number of tracks in the album
    artist = Column(String(150), nullable=False, index=True)  # Artist name (stored as String)
    publish_year = Column(Integer, nullable=True)
    details = Column(String, nullable=False)

    # If we had an Artist model, we would relate it like this:
    # artist_id = Column(Integer, ForeignKey('artists.id'))  # Artist ID
    # artist = relationship("Artist", back_populates="albums")  # Relating the album to the artist
