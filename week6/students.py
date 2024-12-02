students=[]
with open("week6/students.csv","r") as file:
    for line in file:
       name,house = line.rstrip().split(",")
       student={"name":name,"house":house}
       students.append(student)

def name(student):
    return student['name']
def house(student):
    return student['house']

for student in sorted(students, key=house):
    print(f"{student['name']}:{student['house']}")