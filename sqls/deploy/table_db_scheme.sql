-- Deploy unimated:table_db_scheme to mysql

BEGIN;

-- XXX Add DDLs here.
alter table `metatable` add COLUMN `dataframe` Char(200);
alter table `metatable` add COLUMN `dataset` Char(200);
alter table `metatable` add COLUMN `scheme` Char(200);
alter table `metatable` add COLUMN `host` Char(200);
alter table `metatable` add COLUMN `port` INTEGER;

COMMIT;
