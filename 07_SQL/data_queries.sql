--List the following details of each employee: employee number, last name, first name, gender, and salary.
SELECT
employees.emp_no, employees.last_name, employees.first_name, employees.gender, salaries.salary
FROM employees
JOIN salaries
ON employees.emp_no = salaries.emp_no;

--List employees who were hired in 1986.
SELECT
first_name, last_name, hire_date
FROM employees
WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31';

--List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
SELECT
dept_manager.dept_no, 
department.dept_name, 
dept_manager.emp_no, 
employees.last_name, 
employees.first_name, 
dept_manager.from_date, 
dept_manager.to_date
FROM dept_manager
JOIN department
ON dept_manager.dept_no = department.dept_no
JOIN employees
ON dept_manager.emp_no = employees.emp_no;

--List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT
employees.emp_no,
employees.last_name,
employees.first_name,
department.dept_name
FROM employees
JOIN dept_emp
ON employees.emp_no = dept_emp.emp_no
JOIN department
ON dept_emp.dept_no = department.dept_no;

--List all employees whose first name is "Hercules" and last names begin with "B."
SELECT
first_name,
last_name
FROM employees
WHERE first_name ='Hercules' AND last_name like 'B%';

--List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT
employees.emp_no,
employees.last_name,
employees.first_name,
department.dept_name
FROM employees
JOIN dept_emp
ON employees.emp_no = dept_emp.emp_no
JOIN department
ON dept_emp.dept_no = department.dept_no
WHERE department.dept_name = 'Sales';

--List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT
employees.emp_no,
employees.last_name,
employees.first_name,
department.dept_name
FROM employees
JOIN dept_emp
ON employees.emp_no = dept_emp.emp_no
JOIN department
ON dept_emp.dept_no = department.dept_no
WHERE department.dept_name = 'Sales' OR department.dept_name = 'Development';

--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT
last_name,
count(last_name)
FROM employees
group by last_name
order by count(last_name) DESC;

--Evidence in hand, you march into your boss's office and present the visualization. With a sly grin, your boss thanks you for your work. On your way out of the office, you hear the words, "Search your ID number." You look down at your badge to see that your employee ID number is 499942.
SELECT * FROM employees
WHERE emp_no = '499942';
