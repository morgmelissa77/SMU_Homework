-- Query_8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.


SELECT 
	last_name,
	COUNT (emp_no) AS lastNameCount
FROM
	employees
GROUP BY
	last_name
ORDER BY
	LastNameCount DESC;