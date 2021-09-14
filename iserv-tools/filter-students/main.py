import pandas as pd
import datacompy
import platform

from pathlib import Path


def main():
    print("Starting...")

    # get class id
    class_id = input("Please enter the id of your class (like `10B`): ")
    print("\n")

    class_id = class_id.upper()

    class_id_pd = pd.Series(class_id)

    # find input files
    current = str(Path.cwd().absolute())

    # os detection for correct names file direction syntax
    if platform.system() == "Windows":
        prefix = current + "\\"
    else:
        prefix = current + "/"

    # open csv files and parse them into lists (and remove header row)
    # ~ school file
    school_csv = pd.read_csv(open(prefix + "school.csv"), delimiter=",")

    # ~ class file
    class_csv = pd.read_csv(open(prefix + "class.csv"), delimiter=";")

    # set csv metadata (header row [=> fieldnames])
    header_row = "Account,Vorname,Nachname,Status,Erstellt am,Erstellt von,Klasse\n"

    # add class_id as column to the class_csv
    class_csv['Klasse'] = class_id

    # filter class and add those members to the filtered list, which don't appear in the school db
    compare = datacompy.Compare(class_csv, school_csv, join_columns=['Vorname', 'Nachname', 'Klasse'],  # You can also specify a list of columns
                                abs_tol=0.0001,
                                rel_tol=0,
                                df1_name='original',
                                df2_name='new')
    print(compare.df1_unq_rows)

    print("-----")

    for index, student in class_csv.iterrows():
        if student[1] in school_csv.vorname.values and student[2] in school_csv.nachname.values and class_id in school_csv.klasse.values:
            pass
        else:
            print(student[1] + " " + student[2] +
                  " isn't listed in the school db!")

    print("\nFinished!")


if __name__ == "__main__":
    main()
