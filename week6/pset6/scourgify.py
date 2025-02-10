import csv

students=[]
with open("before.csv","r") as file:
   reader=csv.DictReader(file)
   for row in reader:
      first,last=row["name"].split(",")
      house=row["house"]
      students.append({"first":first,'last':last,"house":house})

with open("after.csv",'w',newline="") as f:
   writer=csv.DictWriter(f,fieldnames=["first","last","house"])
   writer.writeheader()
   for student in students:
      writer.writerow({"first":student["first"],"last":student["last"],"house":student["house"]})