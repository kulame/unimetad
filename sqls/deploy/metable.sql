-- Deploy unimated:metable to mysql

BEGIN;

-- XXX Add DDLs here.
CREATE TABLE metatable (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	name VARCHAR(200), 
	meta JSON, 
	created_at DATETIME, 
	producer VARCHAR(200), 
	version INTEGER, 
	sign VARCHAR(200), 
	PRIMARY KEY (id)
);

COMMIT;
