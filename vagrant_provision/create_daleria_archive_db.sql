CREATE DATABASE dukedoms_archive;

CREATE USER dukedoms_archivist WITH PASSWORD 'dukedoms';

ALTER ROLE dukedoms_archivist SET client_encoding TO 'utf8';
ALTER ROLE dukedoms_archivist SET default_transaction_isolation TO 'read committed';
ALTER ROLE dukedoms_archivist SET timezone to 'UTC';
ALTER ROLE dukedoms_archivist WITH CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE dukedoms_archive TO dukedoms_archivist;
