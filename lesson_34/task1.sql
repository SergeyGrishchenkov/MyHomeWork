--write a query in SQL to display the first name, last name, department number, and department name for each employee
/*select
e.first_name,
e.last_name,
e.department_id as DepID,
d.depart_name as DepName
from employees as e
left join departments as d
on d.department_id = e.department_id;*/
--write a query in SQL to display the first and last name, department, city, and state province for each employee
/*select
e.first_name,
e.last_name,
ifnull(d.depart_name, '') as DepName,
ifnull(l.city, '') as City
from employees as e
left join departments as d
on d.department_id = e.department_id
left join locations as l
on l.location_id = d.location_id*/
--write a query in SQL to display the first name, last name, department number, and department name, for all employees for departments 80 or 40
/*select
e.first_name,
e.last_name,
e.department_id as DepID,
d.depart_name as DepName
from employees as e
left join departments as d
on d.department_id = e.department_id
where
d.department_id = 40 or d.department_id = 80;*/

--write a query in SQL to display all departments including those where does not have any employee
/*select
d.department_id as DepID,
d.depart_name as Depname,
ifnull(e.first_name, '') as FirstName,
ifnull(e.last_name, '') as LastName
from departments as d
left join employees as e
on d.department_id = e.department_id*/
--write a query in SQL to display the first name of all employees including the first name of their manager
--НЕТ ТАБЛИЦЫ С ДАННЫМИ МЕНЕДЖЕРОВ
/*select
*
from employees as e*/

--write a query in SQL to display the job title, full name (first and last name ) of the employee, and the difference between the maximum salary for the job and the salary of the employee
/*select
j.job_title as JobTitle,
e.first_name || ' ' || e.last_name as FullName,
j.max_salary - e.salary as Difference
from employees as e
left join jobs as j
on j.job_id = e.job_id;*/

--write a query in SQL to display the job title and the average salary of employees
/*select
j.job_title as JobTitle,
sum(e.salary) / count(e.employee_id) as Average
from jobs as j
left join employees as e
on j.job_id = e.job_id
group by
j.job_title*/

--write a query in SQL to display the full name (first and last name), and salary of those employees who work in any department located in London
/*select
e.first_name || ' ' || e.last_name as FullName,
e.salary as Salary
from locations as l
inner join departments as d
on d.location_id = l.location_id
and l.location_id = 2400
inner join employees as e
on e.department_id = d.department_id*/
--where d.department_id = 1000
--write a query in SQL to display the department name and the number of employees in each department
/*select
d.depart_name as Depname,
count(e.employee_id) as CountOfEmp
from departments as d
left join employees as e
on d.department_id = e.department_id
group by d.depart_name;*/
