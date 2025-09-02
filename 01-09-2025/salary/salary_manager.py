salaries = []

def create_salary(salary):
    global salaries
    salaries.append(salary)

def read_all():
    return salaries

def read_by_salary(salary):
    for I in range(len(salaries)):
        if salaries[I] == salary:
            return I
    return -1 

def update(old_salary, new_salary):
    global salaries
    index = read_by_salary(old_salary)
    salaries[index] = new_salary


def delete_by_salary(salary):
    global salaries
    index = read_by_salary(salary)
    salaries.pop(index)  




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
   