import csv

with open("data/student_data.csv", mode="r", encoding="utf-8") as in_file:
    csv_reader = csv.DictReader(in_file)

    count = 0
    for record in csv_reader:
        if ".edu" in record['email']:
            count += 1
print(count)
