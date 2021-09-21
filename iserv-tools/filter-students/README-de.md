# filter-students

Dieses Skript überprüft, ob sich die Schüler einer IServ-Gruppe auch in der Schuldatenbank (`sibank`) befinden, und listet die Schüler, die nicht enthalten sind. Es listet auch eine Schülerin oder einen Schüler, wenn die Klasse im Datensatz falsch eingetragen.

## Das Skript starten

Um das Skript auszuführen, muss Python 3 installiert sein. Um die notwendigen externen Softwarepackete zu installieren, führen sie zunächst den Befehl `pip3 install -r requirements.txt` aus.

Wenn dann die Daten in `class.csv` und `school.csv` eingetragen sind, können sie das Skript mit

```sh
python3 main.py
```

ausführen.
