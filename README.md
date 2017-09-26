# k-anonymity

TODO: k-anonymity explanation

Dem Programm wird ein Parameter übergeben - k

Anschließend wird der Datensatz aus der cvs Datei (data.cvs) eingelesen.

Dieses Programm ist darauf ausgelegt, drei Quasi Identifikatoren zu behandeln. 
+Geburtsdatum
+Postleitzahl
+Geschlecht

Schritt für Schritt werden die jeweiligen Attribute anonymisiert. Dies geschieht 
global, d.h. ein Anonymisierungsschritt wird auf alle Datensätze angewandt.

Dabei werden alle möglichen Kombinationen durchgetestet. 


| # of date anonymizations | # of zip anonymizations | # of sex anonymizations |
| :----------------------: |:-----------------------:| :----------------------:|
| 0                        | 0                       | 0                       |
| 0                        | 0                       | 1                       |
| 0                        | 1                       | 0                       |
| 0                        | 1                       | 1                       |
| ...                      | ...                     | ...                     |
| 3                        | 3                       | 1                       |
| 3                        | 4                       | 0                       |
| 3                        | 4                       | 1                       |
| ...                      | ...                     | ...                     |
| 6                        | 5                       | 0                       |
| 6                        | 5                       | 1                       |


Bei jeder Iteration wird
der komplette Datensatz in die jeweiligen Äquivalenzklassen gruppiert und das 
'k' ermittelt. Wird das vorgegebene 'k' erreicht, wird die Anzahl der jeweiligen
Anonymisierungsschritte und der Datensatz gespeichert. 
 
Am Ende werden alle Kombinationen die das 'k' erfüllen verglichen. Dies passiert 
durch einen 'Score'. Dabei werden die Anzahl der Schritte zur anonymisierung 
durch die maximale Anzahl an Anonymisierungsschritten dividiert.
Die maximale Anzahl an Schritten wird weiter unten angegeben.

Rersultat des Programmes ist, wieviele Anonymisierungsschritte pro Quasi Identifikator
notwendig sind, um das 'k' zu erreichen und so wenig Information wie möglich zu verlieren.

 
# Quasi Identifikatoren - Anonymisierungsklassen

#### Geburtsdatum

Date format: YYYYMMDD

+ 20170110
+ 201701H1
+ 201701**
+ 2017Q1
+ 20171H
+ 2017
+ 201*
+ 20**
+ 2***
+ '**** 

### ZIP Code 

Annahme: 5 stellige Zahl

+ 12345
+ 1234*
+ 123**
+ 12***
+ 1****
+ '*****

### Geschlecht

+ female/male
+ <nowiki>*</nowiki>

## Example

TODO: example

# Dataset

TODO: explain dataset

# Weaknesses

TODO: describe weaknesses
