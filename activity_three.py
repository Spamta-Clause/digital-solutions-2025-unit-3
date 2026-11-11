import csv
student_id = int(input("Student ID:"))

found = False
with open("data/student_data.csv", mode="r", encoding="utf-8") as in_file:
    csv_reader = csv.DictReader(in_file)
    for record in csv_reader:
        if str(student_id) == record['student_id']:
            found = True
            print(f"Name: {record['first_name']} {record['last_name']}\nEmail: {record['email']}")
if found == False:
    print("Student not found")