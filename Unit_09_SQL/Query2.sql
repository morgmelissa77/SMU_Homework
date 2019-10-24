-- Query_2. List employees who were hired in 1986. 

SELECT 
	emp_no,
	first_name,
	last_name,
	gender,
	hire_date

FROM
	employees
WHERE
	EXTRACT (YEAR FROM hire_date) = 1986
ORDER BY
	last_name ASC;