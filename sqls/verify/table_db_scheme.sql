-- Verify unimated:table_db_scheme on mysql

BEGIN;

-- XXX Add verifications here.
select dataframe,dataset,scheme, host, port from metatable limit 1;
ROLLBACK;
