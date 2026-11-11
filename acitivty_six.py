import csv

with open("data/student_emails.tsv", mode="r", encoding="utf-8") as tsv_file:
    tsv_reader = csv.DictReader(tsv_file, delimiter="\t")

    for record in tsv_reader:
        if record["email"].endswith(".gov"):
            print(f"{record['student_id']}: {record['email']}")