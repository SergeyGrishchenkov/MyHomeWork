select
e.first_name as FirstName,
e.last_name as LastName
from employees as e;
--*******************
select
e.department_id as Departamrnts
from employees as e
GROUP BY e.department_id;
--*******************
select
*
from employees as e
order by
e.first_name DESC;
--*******************
select
e.first_name as FirstName,
e.last_name as LastName,
e.salary as Salary,
e.salary * 0.12 as PF
from employees as e;
--*******************
select
MAX(e.salary) as MaxSalary,
MIN(e.salary) as MinSalary
from employees as e;
--*******************
select
e.first_name as FirstName,
e.last_name as LastName,
e.salary as Salary,
ROUND(e.salary / 12.0, 2) as MonthSalary
from employees as e;
--*******************