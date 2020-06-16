-- 1378. Replace Employee ID With The Unique Identifier
-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

SELECT 
    u.unique_id,
    e.name
FROM
    Employees as e LEFT JOIN EmployeeUNI as u ON e.id = u.id

-- Runtime: 1859 ms, faster than 26.97% of MySQL online submissions for Replace Employee ID With The Unique Identifier.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Replace Employee ID With The Unique Identifier.
