from salary_manager import create_salary, read_all, read_by_salary
from salary_manager import salaries, update, delete_by_salary


create_salary(10000)
create_salary(20000)     
create_salary(30000) 
create_salary(40000) 

result_salaries = read_all()
for salary in result_salaries:
    print(salary)

print(read_by_salary(20000))
print(read_by_salary(50000))
print(salaries[read_by_salary(40000)])


update(30000, 300)
print(read_all())

delete_by_salary(10000)
print(read_all())