-- To be run by role "postgres"

CREATE ROLE geodb_admin CREATEROLE CREATEDB LOGIN password 'xxxxxxxx';
-- Create group roles
CREATE ROLE uwasa_update;
CREATE ROLE uwasa_view;
CREATE ROLE uwasa_codelist;
