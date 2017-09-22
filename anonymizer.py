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


def anonymize_date(persons):
    for p in persons:
        old_dob = p.dob
        if len(old_dob) == 8 and old_dob.isdigit():
            day = int(old_dob[:-2])
            if day in range (16):
                new_dob = old_dob[:6] + '1H'
            else:
                new_dob = old_dob[:6] + '2H'
        elif 'H' in old_dob and len(old_dob) == 8:
            new_dob = old_dob[:6] + '**'
        elif '**' in old_dob and len(old_dob) == 8:
            month = int(old_dob[4:6])
            if month in range(4):
                new_dob = old_dob[:4] + 'Q1'
            elif month in range(4,7):
                new_dob = old_dob[:4] + 'Q2'
            elif month in range(7,10):
                new_dob = old_dob[:4] + 'Q3'
            elif month in range(10,13):
                new_dob = old_dob[:4] + 'Q4'
        elif 'Q' in old_dob:
            if old_dob[-1] in ['1', '2']:
                new_dob = old_dob[:4] + '1H'
            if old_dob[-1] in ['3', '4']:
                new_dob = old_dob[:4] + '2H'
        elif 'H' in old_dob and len(old_dob) == 6:
            new_dob = old_dob[:4]
        elif old_dob.count('*') == 0 and len(old_dob) == 4:
            new_dob = old_dob[:3] + '*'
        elif old_dob.count('*') == 1 and len(old_dob) == 4:
            new_dob = old_dob[:2] + '**'
        elif old_dob.count('*') == 2 and len(old_dob) == 4:
            new_dob = old_dob[:1] + '***'
        elif old_dob.count('*') == 3 and len(old_dob) == 4:
            new_dob = '****'
        else:
            new_dob = old_dob

        p.dob = new_dob
    return persons


def get_combinations_with_least_steps(satisfying_combinations):
    sorted_combinations = sorted(satisfying_combinations, key=lambda combination: combination.get_anonymization_score, reverse=False)
    least_steps = sorted_combinations[0].get_anonymization_score()
    return [combination for combination in sorted_combinations if combination.get_anonymization_score() == least_steps]


def copy_persons(fresh_persons):
    persons = []
    for p in fresh_persons:
        persons.append(Person(p.name, p.dob, p.sex, p.zipcode, p.illness))
    return persons


def group_persons(persons):
    grouped_persons = {}
    for p in persons:
        pseudo_parameters = str(p.dob) + str(p.zipcode) + str(p.sex)
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


def anonymize(persons, iDate, iZip, iSex):
    for i in range(iDate):
        persons = anonymize_date(persons)
    for j in range(iZip):
        persons = anonymize_ZIP(persons)
    for l in range(iSex):
        persons = anonymize_sex(persons)
    return persons


def export_csv(combination):
    print "Exporting CSV ..."
    try:
        csv_list = [["name","date_of_birth","sex","zip","illness"]]
        for index, group in enumerate(combination.grouped_persons):
            for p in combination.grouped_persons[group]:
                csv_entry = str(p).split(', ')
                csv_entry.append("Group " + str(index+1))
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
    for iDate in range(10):
        for iZip in range(6):
            for iSex in range(2):
                persons = copy_persons(fresh_persons)
                persons = anonymize(persons, iDate, iZip, iSex)

                grouped_persons = group_persons(persons)

                k = get_k(grouped_persons)

                if k >= given_k:
                    satisfying_combinations.append(Combination(iDate,iZip,iSex,k,grouped_persons))

    if len(satisfying_combinations) > 0:
        combinations_with_least_steps = get_combinations_with_least_steps(satisfying_combinations)
        best_combination = get_best_combination(combinations_with_least_steps)
        print_results(best_combination)
        export_csv(best_combination)
    else:
        print "No satisfying combinations found. Try again with a lower k!"


if __name__ == "__main__":
    main()
