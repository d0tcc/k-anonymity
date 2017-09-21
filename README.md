# k-anonymity

TODO: k-anonymity explanation

# Quasi identifiers

### Classes for quasi identifier 'Date of Birth':

Date format: YYYYMMDD

+ 20170110
* 201701H1
* 201701**
* 2017Q1
* 20171H
* 2017
* 201*

### Classes for quasi identifier 'ZIP code'

always 5 digits

* 12345
* 1234*
* 123**
* 12***
* 1****
* *****

### Classes for quasi identifier 'sex'

only two possibilities

* female
* <nowiki>*</nowiki>

# Algorithm

In our approach we try all the possible combinations of anonymization steps for the three quasi identifiers (date of birth, zip, sex).

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

## Example

TODO: example

# Dataset

TODO: explain dataset

# Weaknesses

TODO: describe weaknesses
