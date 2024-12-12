import csv
students=[]
with open("week6/students.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        students.append({"name":row[0] and "house":row[1]})

# def get_name(student):
#     return student["name"]
# for line in file:
#        name,house = line.rstrip().split(",")
#        student={"name":name,"house":house}
#        students.append(student)
# def get_house(student):
#     return student["house"]

for student in sorted(students, key=lambda student: student["name"]): #for student in sorted(students, key=get_name): both are same
    print(f"{student['name']}:{student['house']}")