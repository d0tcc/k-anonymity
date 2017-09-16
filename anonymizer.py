import csv
from Person import Person
from Combination import Combination
import sys


def read_csv():
    persons = []
    with open('data.csv', 'rb') as f:
        reader = csv.reader(f)
        raw_persons = list(reader)
    for p in raw_persons[1:]: # first line are the names
        persons.append(Person(p[0], p[1], p[2], p[3], p[4]))
    return persons


def anonymize_sex(persons):
    for p in persons:
        p.sex = ''
    return persons


def anonymize_ZIP(persons):
    for p in persons:
        p.zipcode = p.zipcode[:-1]
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


def get_combinations_with_least_steps(satisfying_combinations):
    sorted_combinations = sorted(satisfying_combinations, key=lambda combination: combination.get_steps, reverse=False)
    least_steps = sorted_combinations[0].get_steps()
    return [combination for combination in sorted_combinations if combination.get_steps() == least_steps]


def copy_persons(fresh_persons):
    persons = []
    for p in fresh_persons:
        persons.append(Person(p.name, p.age[0], p.sex, p.zipcode, p.illness))
    return persons


def group_persons(persons):
    dict = {}
    for p in persons:
        age = str(p.age[0]) + str(p.age[1]) + str(p.zipcode) + str(p.sex)
        if dict.get(age) is None:
            dict[age] = []
        dict[age].append(p)
    return dict

def getK(dict):
    tmpDict = {}
    for group in dict:
        tmpDict[group] = len(dict[group])
    k = None
    for group in tmpDict:
        if tmpDict[group] < k or k is None:
            k = tmpDict[group]
    return k

def print_results(combinations_with_least_steps):
    print "==============="
    print "Anonymized Data"
    print "===============\n"
    for combination in combinations_with_least_steps:
        print combination


def anonymize(persons, iAge, iZip, iSex):
    for i in range(iAge):
        persons = anonymize_age(persons)
    for j in range(iZip):
        persons = anonymize_ZIP(persons)
    for l in range(iSex):
        persons = anonymize_sex(persons)
    return persons


def main():
    try:
        given_k = int(sys.argv[1])
    except:
        print "Please enter a valid value for k! Usage example: python anonymizer.py 4"
        exit()
    satisfying_combinations = []
    fresh_persons = read_csv()
    for iAge in range(8):
        for iZip in range(6):
            for iSex in range(2):
                persons = copy_persons(fresh_persons)
                persons = anonymize(persons, iAge, iZip, iSex)

                grouped_persons = group_persons(persons)

                k = getK(grouped_persons)

                if k >= given_k:
                    satisfying_combinations.append(Combination(iAge,iZip,iSex,k,grouped_persons))

    combinations_with_least_steps = get_combinations_with_least_steps(satisfying_combinations)

    print_results(combinations_with_least_steps)


if __name__ == "__main__":
    main()
