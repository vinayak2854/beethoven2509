employees = []
def create_employee(id, name, job_title, salary, join_date):
    emp = {
        'id':id, 
        'name': name, 
        'job_title': job_title, 
        'salary': salary, 
        'join_date': join_date
    }
    employees.append(emp)
def read_all():
    return employees