import csv

with open("data/student_data.csv", mode="r", encoding="utf-8") as in_file:
    csv_reader = csv.reader(in_file)
    next(csv_reader)

    students_read = 0
    for record in csv_reader:
        print(f"{record[1]} {record[2]}: {record[3]}")
        students_read += 1
        if students_read == 5:
            break
