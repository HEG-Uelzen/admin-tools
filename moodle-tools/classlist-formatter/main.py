import os
import json
import string
import platform

from time import sleep
from pathlib import Path
from progress.bar import Bar
from progress.spinner import Spinner


def main():
    # file_url = input("Enter the direction of your JSON-file: ")
    
    # find names.json file
    current = str(Path.cwd().absolute())
    
    # os detection for correct names file direction syntax
    if platform.system() == "Windows":
        file_url = current + "\\names.json"

    else:
        file_url = current + "/names.json"

    print("--------------------")
    print("| Programm started |")
    print("--------------------")

    final = []

    # read file 
    names = json.loads(open(file_url).read())
    # print(names)

    # password input
    password = input("Please enter the default password for your students: ")
    password = str(password)
    print("You set " + password + " as default password.")

    # email domain input
    e_domain = input("Please enter the E-Mail Domain of your students: ")
    print("You set " + e_domain + " as your studendts e-mail domain.")
    
    print()
    print("-----------------------------------------------------------------")
    print()
    sleep(1)
    
    # create progress bar for the name formatting process
    bar = Bar("Processing", max=len(names))
    
    # iterate over given names => name formatting process
    for name in names:
        
        # generate username
        name_lowercase = name.lower()
        # print(name_lowercase)

        username = name_lowercase.replace(" ", ".")
        username = str(username)
        # print(username)
        
        # generate first- and lastname
        vornachname = name.split(' ')

        firstname = vornachname[0]
        firstname = str(firstname)

        lastname = vornachname[1]
        lastname = str(lastname)
        
        # generate user email-adress
        email = username + "@" + e_domain
        email = str(email)
        # print(email)
        
        # generate line in the textfile for the handled user
        final_line = username + ";" + password + ";" + firstname + ";" + lastname + ";" + email
        # print(final_line)
        
        # add final user output to all of the other finally formatted users
        final.append(final_line)

        bar.next()
        sleep(0.1)

    bar.finish()

    print()
    print("Creating output file...")
    print()
    sleep(1)
    
    # open the output file
    output_file = open("output.txt", "w+")
    
    # create progress bar for the output-file writing process
    spinner = Spinner("Writing...")

    # write first static line that tells moodle the format
    output_file.write('username;password;firstname;lastname;email' + '\n')

    # write each finally formatted user to the output file
    for item in final:
        output_file.write(item + '\n')
        spinner.next()
        sleep(0.1)

    spinner.finish()

        

    
if __name__ == "__main__":
    main()
