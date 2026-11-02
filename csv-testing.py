import csv

with open("data/student_data.csv", mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    header = next(csv_reader)
    print(header)

    for row in csv_reader:
        student_id = int(row[0])
        if student_id > 395:
            print(f"{student_id}: {row[1]} {row[2]}")