-- Verify unimated:metable on mysql

BEGIN;

-- XXX Add verifications here.
select 1 from metatable limit 1;
ROLLBACK;
