import csv
import platform

from pathlib import Path


def filterteachers():
    print("Starting...")
    # find input files
    current = str(Path.cwd().absolute())

    # os detection for correct names file direction syntax
    if platform.system() == "Windows":
        prefix = current + "\\"
    else:
        prefix = current + "/"

    # open csv files and parse them into lists (and remove header row)
    # ~ teachers file
    teachers_csv = csv.reader(open(prefix + "teachers.csv"), delimiter=";")
    teachers_raw = list(teachers_csv)[1:]

    # ~ classlist file
    classlist_csv = csv.reader(open(prefix + "classlist.csv"), delimiter=";")
    classlist_raw = list(classlist_csv)[1:]

    # set csv metadata (header row [=> fieldnames] and csv dialect)
    meta_row_reader = csv.DictReader(
        open(prefix + "classlist.csv"), delimiter=";")
    header_row = meta_row_reader.fieldnames
    csv_dialect = csv.register_dialect(
        'userlist', 'excel', delimiter=';')

    # create empty list where all students get temporarily saved
    students = []

    # filter classlist and only add those members to the students list, which don't appear in the teacher list
    for member in classlist_raw:
        if teachers_raw.__contains__(member):
            pass
        else:
            students.append(member)

    # open/create output students.csv file
    with open("students.csv", "w+", encoding="UTF-8") as students_file:
        writer = csv.writer(students_file, dialect='userlist')

        # write header row
        writer.writerow(header_row)

        # write students
        writer.writerows(students)

    print("\nFinished!")


if __name__ == "__main__":
    filterteachers()
