# Write your MySQL query statement below
SELECT s.machine_id, ROUND(avg(e.timestamp-s.timestamp),3) AS processing_time
FROM Activity s
JOIN Activity e
ON s.process_id = e.process_id
AND s.machine_id = e.machine_id
WHERE s.activity_type = 'start' AND e.activity_type = 'end' 
GROUP BY machine_id