import csv

with open("before.csv", "r") as infile, open("after.csv", "a", newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    # Write the header only once
    writer.writeheader()
    
    for row in reader:
        first, last = row["name"].split(",")
        writer.writerow({"first": first.rstrip(), "last": last.rstrip(), "house": row["house"].rstrip()})
