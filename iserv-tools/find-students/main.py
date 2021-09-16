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

    school_query_string = 'Klasse == "' + class_id + '"'
    school_csv = school_csv.query(school_query_string)

    # filter class and add those members to the filtered list, which don't appear in the school db
    compare = datacompy.Compare(school_csv, class_csv, join_columns=['Vorname', 'Nachname', 'Klasse'],  # You can also specify a list of columns
                                abs_tol=0.0001,
                                rel_tol=0,
                                df1_name='school',
                                df2_name='class')
    print(compare.df1_unq_rows)

    print("-----")

    print("\nFinished!")


if __name__ == "__main__":
    main()
