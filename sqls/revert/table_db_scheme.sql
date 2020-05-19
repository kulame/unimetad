-- Revert unimated:table_db_scheme from mysql

BEGIN;

-- XXX Add DDLs here.
alter table `metatable` drop column `dataframe`;
alter table `metatable` drop column `dataset`;
alter table `metatable` drop column `scheme`;
alter table `metatable` drop column `host`;
alter table `metatable` drop column `port`;
COMMIT;