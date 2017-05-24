psql

CREATE DATABASE fraud;

\c fraud

CREATE TABLE new_events (
payout_type smallint,
fb_published smallint,
org_facebook double precision,
has_analytics double precision,
has_header int,
org_twitter double precision,
account_life double precision,
event_life double precision,
eu_currency int,
payout_count double precision,
total_payout double precision,
ticket_sales_amount double precision,
ticket_sales_count double precision,
wc_description double precision
);
