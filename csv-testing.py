import csv

with open("data/student_data.csv", mode="r", encoding="utf-8") as in_file:
    csv_reader = csv.reader(in_file)

    with open("data/students_data.tsv", mode="w", encoding="utf-8", newline="") as out_file:
        tsv_writer = csv.writer(out_file, delimiter="\t")
        tsv_writer.writerows(csv_reader)