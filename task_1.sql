--Listing course names
SELECT name
FROM courses

--Listing teachers names
SELECT name
FROM teachers


--Listing teacher who takes the highest number of courses

SELECT TOP 1 teacher_id
FROM  ( SELECT teacher_id,
               COUNT(teacher_id) as "teacher_id_count"
        FROM courses
        GROUP BY teacher_id
        ORDER BY "teacher_id_count" DESC )

--Listing teachers who do not take any courses

SELECT id 
FROM teachers as x
WHERE NOT EXISTS
(
   SELECT teacher_id 
   FROM courses as y
   WHERE x.id = y.id
)
