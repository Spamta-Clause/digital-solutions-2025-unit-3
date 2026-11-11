import csv

with open("data/student_data.csv", mode="r", encoding="utf-8") as in_file:
    reader = csv.DictReader(in_file)
    with open("data/student_emails.tsv", mode="w", encoding="utf-8", newline="") as out_file:
        writer = csv.writer(out_file, delimiter="\t")
        writer.writerow(["student_id", "email"])

        for record in reader:
            writer.writerow([record["student_id"], record["email"]])
