# classlist-formatter (moodle-tools)

Little python script that generates a list of new users out of a name list for the moodel edu system.

### example input (json formatted)
```json
[
    "Liam Meyer",
    "Noah Gustav",
    "William Dumbledore",
    "James Granger",
    "Logan Müller",
    "Benjamin Blümchen",
    "Mason Briant",
    "Elijah Schwarzkopf",
    "Oliver Krummnase",
    "Jacob Milk",
    "Lucas Podolski",
    "Michael Schuhmacher",
    "Alexander Maschallah"                                                                                                                       
]
```

#### Output (txt):
```txt
username;password;firstname;lastname;email
liam.meyer;InitialPassword;Liam;Meyer;liam.meyer@email-domain-of-users.com
noah.gustav;InitialPassword;Noah;Gustav;noah.gustav@email-domain-of-users.com
william.dumbledore;InitialPassword;William;Dumbledore;william.dumbledore@email-domain-of-users.com
james.granger;InitialPassword;James;Granger;james.granger@email-domain-of-users.com
logan.mueller;InitialPassword;Logan;Müller;logan.mueller@email-domain-of-users.com
benjamin.bluemchen;InitialPassword;Benjamin;Blümchen;benjamin.bluemchen@email-domain-of-users.com
mason.briant;InitialPassword;Mason;Briant;mason.briant@email-domain-of-users.com
elijah.schwarzkopf;InitialPassword;Elijah;Schwarzkopf;elijah.schwarzkopf@email-domain-of-users.com
oliver.krummnase;InitialPassword;Oliver;Krummnase;oliver.krummnase@email-domain-of-users.com
jacob.milk;InitialPassword;Jacob;Milk;jacob.milk@email-domain-of-users.com
lucas.podolski;InitialPassword;Lucas;Podolski;lucas.podolski@email-domain-of-users.com
michael.schuhmacher;InitialPassword;Michael;Schuhmacher;michael.schuhmacher@email-domain-of-users.com
alexander.maschallah;InitialPassword;Alexander;Maschallah;alexander.maschallah@email-domain-of-users.com
```

## installation
1. Clone the repo with `git clone https://github.com/HEG-Uelzen/moodle-classlist-formatter.git` and navigate into the directory with `cd moodle-classlist-formatter`
2. Install the python dependencies with `pip3 install -r requirements.txt`
3. execute the tool with `python3 main.py`
