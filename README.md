# k-anonymity

## Algorithmus

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

 
## Quasi Identifikatoren - Anonymisierungsklassen

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

Datensatz:

| Gebustsdatum      | ZIP   | Geschlecht | Krankheit |
| :---------------: |:-----:| :---------:| :--------:|
| 19780808          | 72021 | male       | Cancer    |
| 19980102          | 63331 | female     | Strain    |
| 19780809          | 72062 | male       | Cancer    |
| 19980329          | 63409 | female     | Dementia  |

### Schritt 1:

| # of date anonymizations | # of zip anonymizations | # of sex anonymizations |
| :----------------------: |:-----------------------:| :----------------------:|
| 1                        | 0                       | 0                       |

| Äquivalenzklasse | Gebustsdatum      | ZIP   | Geschlecht | Krankheit |
| :---------------:| :---------------: |:-----:| :---------:| :--------:|
| 1                | 197808H1          | 72021 | male       | Cancer    |
| 2                | 199801H1          | 63331 | female     | Strain    |
| 3                | 197808H1          | 72062 | male       | Cancer    |
| 4                | 199803H2          | 63409 | female     | Dementia  |

...

### Schritt 6

| # of date anonymizations | # of zip anonymizations | # of sex anonymizations |
| :----------------------: |:-----------------------:| :----------------------:|
| 4                        | 2                       | 0                       |

| Äquivalenzklasse | Gebustsdatum    | ZIP   | Geschlecht | Krankheit |
|:---------------: | :-------------: |:-----:| :---------:| :--------:|
| 1                | 1978H2          | 720** | male       | Cancer    |
| 2                | 1998H1          | 633** | female     | Strain    |
| 1                | 1978H2          | 720** | male       | Cancer    |
| 3                | 1998H1          | 634** | female     | Dementia  |

### Schritt 7

| # of date anonymizations | # of zip anonymizations | # of sex anonymizations |
| :----------------------: |:-----------------------:| :----------------------:|
| 4                        | 3                       | 0                       |

| Äquivalenzklasse | Geburtsdatum    | ZIP   | Geschlecht | Krankheit |
|:---------------: | :-------------: |:-----:| :---------:| :--------:|
| 1                | 1978H2          | 72*** | male       | Cancer    |
| 2                | 1998H1          | 63*** | female     | Strain    |
| 1                | 1978H2          | 72*** | male       | Cancer    |
| 2                | 1998H1          | 63*** | female     | Dementia  |

Insgesamt 7 Anonymisierungsschritte. Score: 4/10 + 3/6 + 0/2 = 0.4 + 0.5 = 0.9

## Datensatz

Der Datensatz muss aus folgenden Attributen bestehen:
+ Name
+ Geburtsdatum: YYYYMMDD
+ Geschlecht: male/female
+ ZIP: 5 Ziffern
+ Krankheit

## Grenzen

Gibt es einen extremen Ausreißer, kommt dieser herangehensweise an ihre Grenzen.

Angenommen folgender Datensatz ist gegeben:

| Gebustsdatum      | ZIP   | Geschlecht | Krankheit |
| :---------------: |:-----:| :---------:| :--------:|
| 20010808          | 92021 | male       | Cancer    |
| 19980102          | 63331 | female     | Strain    |
| 19780809          | 72062 | male       | Cancer    |
| 19980329          | 63409 | female     | Dementia  |
| 19970423          | 22321 | male       | Cancer    |
| 19980322          | 53531 | female     | Strain    |
| 19540512          | 32462 | male       | Cancer    |
| 19880321          | 63634 | female     | Dementia  |

Hier muss das Geburtsdatum und die Postleitzahl komplett anonymisiert werden,
um zumindest k = 2 zu erreichen.
Das Problem ist, dass die Anonymisierungsschritte global durchgeführt werden und
 fix vorgegeben sind.

