# k-anonymity

Altersklassen:
viele kleine Klassen (1 Jahr), 2 Jahre, 4, 8, 16, 32, 64, 128
Basisklasse ist 1. Die Schritte sind:

1) zu 2 Jahren zusammenfassen
2) zu 4 Jahren zusammenfassen
3) zu 8 Jahren zusammenfassen
4) zu 16 Jahren zusammenfassen
5) zu 32 Jahren zusammenfassen
6) zu 64 Jahren zusammenfassen
7) zu 128 Jahren zusammenfassen


PLZ-Klassen:
5 Stellen, 4, 3, 2, 1, 0 (völlig anonymisiert)
Basisklasse ist 5 Stellen. Die Schritte sind:

1) auf 4 Stellen verringern
2) auf 3 Stellen verringern
3) auf 2 Stellen verringern
4) auf 1 Stellen verringern
5) auf 0 Stellen verringern

maximal 2^14 mögliche Kombinationen an Schritten der Anonymisierung (maximal weil wir hoffentlich bei einen Wegen schon früher das gewünschte k erreichen und damit einige Wege sparen)

Parameter: csv-File, k

Rekursive Funktion:
geht binären Baum durch. Mögliche Schritte: A (Age) oder Z (Zip), linker oder rechter Weg. Probiert diese Kombination aus: wenn in dieser Variation die kleinste Äquivalenzklasse größer gleich dem gegebenen k ist, wird diese Kombination (inklusive dem erreichten k) zu einer Liste hinzugefügt.
Bei einem erfolgreichen k gehen wir den Weg nicht weiter, da ja das Ziel schon bei geringerem Anonymisierungsgrad erreicht wurde.

Als Ergebnis bekommen wir eine Liste mit möglichen Wegen, um das Ziel von k zu erreichen.
Der Weg (z.B. "AZZAAZ") mit der geringsten Länge ist unser Ergebnis.
Wenn es mehrere mit der gleichen Länge gibt, wir zusätzlich auf das erreichte k geschaut und der Weg mit dem größten k als Ergebnis herangenommen. Falls es hier auch mehrere gibt, wird das Ergebnis mit der geringsten Spanne genommen (niedrigste Anzahl an Elementen in einer Klasse, größte Anzahl an Elementen in einer Klasse)
