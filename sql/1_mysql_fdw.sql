ALTER DATABASE luwasa SET SEARCH_PATH TO codelist, core, settings, maxcom, topology, useful_views, public;

DROP SCHEMA IF EXISTS maxcom CASCADE ;
DROP SERVER IF EXISTS mysql_server CASCADE;

CREATE SERVER mysql_server
     FOREIGN DATA WRAPPER mysql_fdw
     OPTIONS (host 'localhost', port '3306');

CREATE USER MAPPING FOR PUBLIC
SERVER mysql_server
OPTIONS (username 'root', password 'Root1234****');

CREATE SCHEMA maxcom;
GRANT USAGE ON SCHEMA maxcom TO PUBLIC;
SET SEARCH_PATH TO maxcom, public;

CREATE FOREIGN TABLE mx_customer(
  id INT,
  cons_name VARCHAR(255),
  conn_date DATE,
  house_no VARCHAR(255),
  address VARCHAR(255),
  city VARCHAR(255),
  status VARCHAR(255),
  tariff_category_master_id INT,
  id_number VARCHAR(255),
  can VARCHAR(255)
)
SERVER mysql_server
     OPTIONS (dbname 'watererp', table_name 'cust_details');

GRANT SELECT ON mx_customer TO uwasa_view, uwasa_update;


CREATE FOREIGN TABLE mx_complaint(
     id INT,
     complaint_date DATE
)
SERVER mysql_server
     OPTIONS (dbname 'watererp', table_name 'customer_complaints');

GRANT SELECT ON mx_complaint TO uwasa_view, uwasa_update;


CREATE FOREIGN TABLE mx_application(
     id INT,
     first_name VARCHAR(255),
     middle_name VARCHAR(255),
     last_name VARCHAR(255)
)
SERVER mysql_server
     OPTIONS (dbname 'watererp', table_name 'application_txn');

GRANT SELECT ON mx_application TO uwasa_view, uwasa_update;

CREATE FOREIGN TABLE mx_meter_details(
  id INT,
  meter_id VARCHAR(255),
  meter_no VARCHAR(255)
)
SERVER mysql_server
     OPTIONS (dbname 'watererp', table_name 'meter_details');

GRANT SELECT ON mx_meter_details TO uwasa_view, uwasa_update;

CREATE FOREIGN TABLE mx_water_leakage_complaint(
  id INT,
  leakage_type VARCHAR(255)
)
SERVER mysql_server
     OPTIONS (dbname 'watererp', table_name 'water_leakage_complaint');

GRANT SELECT ON mx_water_leakage_complaint TO uwasa_view, uwasa_update;

CREATE FOREIGN TABLE mx_tariff_category(
  id INT,
  tariff_category VARCHAR(255),
  type VARCHAR(255)
)
SERVER mysql_server
     OPTIONS (dbname 'watererp', table_name 'tariff_category_master');

GRANT SELECT ON mx_tariff_category TO uwasa_view, uwasa_update;

CREATE FOREIGN TABLE mx_bill_details(
  id INT,
  can VARCHAR(255),
  met_reading_dt DATE,
  initial_reading NUMERIC,
  present_reading NUMERIC
)
SERVER mysql_server
     OPTIONS (dbname 'watererp', table_name 'bill_details');

GRANT SELECT ON mx_bill_details TO uwasa_view, uwasa_update;


CREATE OR REPLACE VIEW mx_last_month_consumption AS
SELECT customer_id, consumption FROM
  (
    SELECT
      b.id                                  AS customer_id,
      d.met_reading_dt,
      d.present_reading - d.initial_reading AS consumption,
      rank()
      OVER (PARTITION BY b.id
        ORDER BY d.met_reading_dt DESC)     AS position
    FROM mx_customer b LEFT JOIN mx_bill_details d ON b.can = d.can
    WHERE extract(MONTH FROM met_reading_dt) = extract(MONTH FROM current_date) - 1
  ) xxx WHERE position = 1;

GRANT SELECT ON mx_last_month_consumption TO uwasa_update, uwasa_view;