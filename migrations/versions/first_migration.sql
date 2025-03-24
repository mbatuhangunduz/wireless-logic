BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 8707241d21a6

CREATE TABLE albums (
    id SERIAL NOT NULL, 
    title VARCHAR(150) NOT NULL, 
    is_published BOOLEAN, 
    track_count INTEGER NOT NULL, 
    artist VARCHAR(150) NOT NULL, 
    PRIMARY KEY (id)
);

CREATE INDEX ix_albums_artist ON albums (artist);

CREATE INDEX ix_albums_id ON albums (id);

CREATE INDEX ix_albums_title ON albums (title);

INSERT INTO alembic_version (version_num) VALUES ('8707241d21a6') RETURNING alembic_version.version_num;

COMMIT;

