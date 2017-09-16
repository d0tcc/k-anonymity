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

def anonymize_age(persons):
    for p in persons:
        from_age = p.age[0]
        to_age = p.age[1]
        age_range = to_age - from_age + 1
        modulo = from_age % (age_range*2)

        if modulo < age_range:
            new_from_age = from_age
            new_to_age = to_age + age_range
        else:
            new_from_age = from_age - age_range
            new_to_age = to_age

        p.age = (new_from_age, new_to_age)
    return persons


def main():
    persons = read_csv()
    persons = anonymize_ZIP(persons)
    for i in range(3):
        persons = anonymize_age(persons)
    for p in persons:
        print p


if __name__ == "__main__":
    main()
