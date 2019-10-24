-- Query_5. List all employees whose first name is "Hercules" and last names begin with "B."

SELECT 
	emp_no,
	first_name,
	last_name,
	gender
FROM
	employees
WHERE
	first_name = 'Hercules'
AND last_name LIKE 'B%';