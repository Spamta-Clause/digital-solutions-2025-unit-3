import csv

with open("data/student_data.csv", mode="r", encoding="utf-8") as in_file:
    csv_reader = csv.DictReader(in_file)

    with open("data/edu_students.csv", mode="w", encoding="utf-8", newline="") as out_file:
        csv_writer = csv.DictReader(out_file, ['student_id', "first_name", 'last_name', 'email'])

        fieldnames = ["student_id", "first_name", "last_name", "email"]
        csv_writer = csv.DictWriter(out_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for record in csv_reader:
            if ".edu" in record['email']:
                csv_writer.writerow({"student_id": record["student_id"], "first_name": record["first_name"], "last_name": record["last_name"], "email": record["email"]})