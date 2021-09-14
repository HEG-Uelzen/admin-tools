# filter-students

This script check's if the students of an IServ group are in the student database `sibank`, and list's them if not so. It also list a student, if the entered class id isn't matching to the students entry in the student database.


## run the script

To run the script you just need python 3 to be installed. To install the required packages(f.e. pandas for the [csv] data handling), run `pip3 install -r requirements.txt` in this directory. Then just ensure your data is placed in `class.csv` and `school.csv`; then run 
```sh
python3 main.py
```
to execute the script.