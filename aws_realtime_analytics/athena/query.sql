-- Query to retrieve events from the last 24 hours
SELECT * FROM "s3_database"."events_table"
WHERE event_time >= current_date - interval '1' day;
