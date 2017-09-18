import csv
from Person import Person
from Combination import Combination
import sys
import math

def read_csv():
    persons = []
    with open('data.csv', 'rb') as f:
        reader = csv.reader(f)
        raw_persons = list(reader)
    for p in raw_persons[1:]: # first line are the names
        persons.append(Person('*', p[1], p[2], p[3], p[4]))
    return persons


def anonymize_sex(persons):
    for p in persons:
        p.sex = ''
    return persons


def anonymize_ZIP(persons):
    for p in persons:
        p.zipcode = p.zipcode[:-1]
    return persons


def sort_persons(persons):
    return sorted(persons, key=lambda person: person.age[0], reverse=False)

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

def anonymize_age_advanced(persons, round):
    sorted_age_persons = sort_persons(persons)
    anonymized_persons = []
    sector_size = int(math.pow(2,round))
    for i in range(int(len(sorted_age_persons)/(2*(round+1)))):
        sector_one = sorted_age_persons[:sector_size]
        sector_two = sorted_age_persons[sector_size:sector_size*2]
        sorted_age_persons = sorted_age_persons[sector_size*2:]

        if len(sorted_age_persons) == 1:
            person_three = sorted_age_persons.pop()
            sector_two.append(person_three)

        from_age = sector_one[0].age[0]
        to_age = sector_two[-1].age[1]

        for p in sector_one:
            p.age = (from_age,to_age)
            anonymized_persons.append(p)
        for p in sector_two:
            p.age = (from_age, to_age)
            anonymized_persons.append(p)

    return anonymized_persons


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
    grouped_persons = {}
    for p in persons:
        pseudo_parameters = str(p.age[0]) + str(p.age[1]) + str(p.zipcode) + str(p.sex)
        if grouped_persons.get(pseudo_parameters) is None:
            grouped_persons[pseudo_parameters] = []
        grouped_persons[pseudo_parameters].append(p)
    return grouped_persons

def get_k(grouped_persons):
    tmpDict = {}
    for group in grouped_persons:
        tmpDict[group] = len(grouped_persons[group])
    k = None
    for group in tmpDict:
        if tmpDict[group] < k or k is None:
            k = tmpDict[group]
    return k

def print_results(best_combination):
    print "==============="
    print "Anonymized Data"
    print "===============\n"
    print best_combination


def anonymize(persons, iAge, iZip, iSex):
    for i in range(iAge):
        persons = anonymize_age_advanced(persons, i)
    for j in range(iZip):
        persons = anonymize_ZIP(persons)
    for l in range(iSex):
        persons = anonymize_sex(persons)
    return persons

def export_csv(combination):
    print "Exporting CSV ..."
    try:
        csv_list = [["Name","Alter","Geschlecht","PLZ","Krankheit","Gruppe"]]
        for index, group in enumerate(combination.grouped_persons):
            for p in combination.grouped_persons[group]:
                csv_entry = str(p).split(', ')
                csv_entry.append("Gruppe " + str(index+1))
                csv_list.append(csv_entry)
        with open("anonymized.csv", 'wb') as myfile:
            wr = csv.writer(myfile, delimiter=",")
            wr.writerows(csv_list)
        print "Successfully exported CSV!"
    except Exception as e:
        print "Error while exporting CSV: " + str(e)

def get_best_combination(combinations_with_least_steps):
    best_combination = None
    tmp_lowest_range = None
    for c in combinations_with_least_steps:
        highest_amount = None
        lowest_amount = None
        tmpDict = {}
        for group in c.grouped_persons:
            tmpDict[group] = len(c.grouped_persons[group])
        for group in tmpDict:
            if tmpDict[group] > highest_amount or highest_amount is None:
                highest_amount = tmpDict[group]
            if tmpDict[group] < lowest_amount or lowest_amount is None:
                lowest_amount = tmpDict[group]
        amount_range = highest_amount - lowest_amount
        if amount_range < tmp_lowest_range or tmp_lowest_range is None:
            best_combination = c
        elif amount_range == tmp_lowest_range:
            if c.k > best_combination.k:
                best_combination = c
    return best_combination

def main():
    try:
        given_k = int(sys.argv[1])
    except:
        print "Please enter a valid value for k! Usage example: python anonymizer.py 4"
        exit()
    satisfying_combinations = []
    fresh_persons = read_csv()
    for iAge in range(4):
        for iZip in range(6):
            for iSex in range(2):
                persons = copy_persons(fresh_persons)
                persons = anonymize(persons, iAge, iZip, iSex)

                grouped_persons = group_persons(persons)

                k = get_k(grouped_persons)

                if k >= given_k:
                    satisfying_combinations.append(Combination(iAge,iZip,iSex,k,grouped_persons))

    if len(satisfying_combinations) > 0:
        combinations_with_least_steps = get_combinations_with_least_steps(satisfying_combinations)
        best_combination = get_best_combination(combinations_with_least_steps)
        print_results(best_combination)
        export_csv(best_combination)
    else:
        print "No satisfying combinations found. Try again with a lower k!"
if __name__ == "__main__":
    main()
