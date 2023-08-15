import pandas as pd
import datacompy
import platform

from pathlib import Path
from time import sleep

CURRENT_PATH = str(Path.cwd().absolute())

# os detection for correct names file direction syntax
if platform.system() == "Windows":
    SEPERATOR = "\\"
else:
    SEPERATOR = "/"

PREFIX = CURRENT_PATH + SEPERATOR


def main():
    filterteachers()

    print("Die Lehrer wurden erfolgreich aus den IServ-Klassengruppen herausgefiltert!")
    print()
    sleep(0.1)

    findstudents()

    print()
    print("Datenverarbeitung beendet!")

# this functions removes all teachers from the input dataset
def filterteachers():
    # get teacher list
    teachers = pd.read_csv(open(PREFIX + "data" + SEPERATOR + "teachers.csv"), delimiter=";")

    # delete unnecessary data
    teachers = teachers.drop(columns=["Status","Erstellt am","Erstellt von","Interne ID","Benutzertyp","Import-ID","Klasse/Information","E-Mail-Adresse","Gruppen"])

    # loop over input files
    pathlist = Path(PREFIX + "data" + SEPERATOR + "input").glob('**/*.csv')

    for filePath in pathlist:
        # open raw class csv
        classlist = pd.read_csv(open(filePath), delimiter=";")

        # delete unnecessary data
        classlist = classlist.drop(columns=["Status","Erstellt am","Erstellt von","Interne ID","Benutzertyp","Import-ID","Klasse/Information","E-Mail-Adresse","Gruppen"])

        # delete all rows which appear in the teacher list
        classlist = classlist[~classlist['Account'].isin(teachers['Account'])] 

        # generate path for new file
        export_directory = str(filePath)
        export_directory = export_directory.split(".")
        export_directory.insert(1,"students.")
        export_dir = ''.join(export_directory)
        export_dir = export_dir.replace("input", "output")
        
        classlist.to_csv(export_dir, index=False, header=True)
        

def findstudents():
    # loop over filtered input files
    pathlist = Path(PREFIX + "data" + SEPERATOR + "output").glob('**/*.csv')

    for filePath in pathlist:
        # get class id
        filteredPath = str(filePath)
        filteredPath = filteredPath.split(SEPERATOR)[-1]
        class_id = filteredPath.split(".")[0]
        class_id = class_id.replace("students", "")

        # open csv files and parse them into dataframes
        # ~ school file
        school = pd.read_csv(open(PREFIX + "data" + SEPERATOR + "school.csv"), delimiter=",")
        
        # ~ class file
        class_csv = pd.read_csv(open(filePath), delimiter=",")
        class_csv = class_csv.drop(columns=["Account"])

        class_csv['Klasse'] = class_id

        school_query_string = 'Klasse == "' + class_id + '"'
        school = school.query(school_query_string)

        # filter class and add those members to the filtered list, which don't appear in the school db
        compare = datacompy.Compare(school, class_csv, join_columns=['Vorname', 'Nachname', 'Klasse'],  # You can also specify a list of columns
                                    abs_tol=0.0001,
                                    rel_tol=0,
                                    df1_name='school',
                                    df2_name='class')
             
        print("Klasse: " + class_id)
        print(compare.df1_unq_rows)
        print(compare.df2_unq_rows)
        print()



if __name__ == "__main__":
    main()
