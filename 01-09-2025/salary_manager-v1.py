salaries = []
salaries.append(100)
salaries.append(500)
salaries.append(800)

print(salaries)

search = 500
index = -1

I = 0
for salary in salaries:
    if salary == search:
        index = I
        break
    I += 1
    
print(index)
salaries.remove(search)
print(salaries)   