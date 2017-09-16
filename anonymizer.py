import csv
from Person import Person


def read_csv():
    persons = []
    with open('data.csv', 'rb') as f:
        reader = csv.reader(f)
        raw_persons = list(reader)
    del raw_persons[0]
    for p in raw_persons:
        persons.append(Person(p[0], p[1], p[2], p[3], p[4]))
    return persons


def anonymize_ZIP(persons):
    for p in persons:
        p.zipcode = p.zipcode[:-1]
    # zipcode = p.zipcode
    # index = zipcode.find('*')
    # p.zipcode = zipcode.replace(index-1,'*')
    return persons

def anonymize_age():
    # TODO
    pass


def main():
    persons = read_csv()
    persons = anonymize_ZIP(persons)
    for p in persons:
        print p


if __name__ == "__main__":
    main()
