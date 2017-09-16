import csv
from Person import Person
from Combination import Combination


def read_csv():
    persons = []
    with open('data.csv', 'rb') as f:
        reader = csv.reader(f)
        raw_persons = list(reader)
    del raw_persons[0]
    for p in raw_persons:
        persons.append(Person(p[0], p[1], p[2], p[3], p[4]))
    return persons


def anonymize_sex(persons):
    for p in persons:
        p.sex = '*'
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


def get_combinations_with_least_steps(satisfying_combinations):
    # TODO
    sorted_combinations = sorted(satisfying_combinations, key=lambda combination: combination.k, reverse=True)
    highest_k = sorted_combinations[0].k
    return [combination for combination in sorted_combinations if combination.k == highest_k]


def copyPersons(fresh_persons):
    persons = []
    for p in fresh_persons:
        persons.append(Person(p.name, p.age[0], p.sex, p.zipcode, p.illness))
    return persons


def groupPersons(persons):
    dict = {}
    for p in persons:
        age = str(p.age[0]) + str(p.age[1]) + str(p.zipcode) + str(p.sex)
        if dict.get(age) is None:
            dict[age] = []
        dict[age].append(p)
    for group in dict:
        dict[group] = len(dict[group])
    k = None
    for group in dict:
        if dict[group] < k or k is None:
            k = dict[group]
    return k


def main():
    given_k = 4
    satisfying_combinations = []
    fresh_persons = read_csv()
    for iAge in range(8):
        for iZip in range(6):
            for iSex in range(2):
                persons = copyPersons(fresh_persons)
                for i in range(iAge):
                    persons = anonymize_age(persons)
                for j in range(iZip):
                    persons = anonymize_ZIP(persons)
                for l in range(iSex):
                    persons = anonymize_sex(persons)

                k = groupPersons(persons)
                if k >= given_k:
                    print "Age: " + str(iAge) + " Zip: " + str(iZip) + " Sex: " + str(iSex)
                    print k

                    #k = get_k(persons)
                #if k >= given_k:
                #    satisfying_combinations.append(Combination(iAge,iZip,iSex,k))

    #combinations_with_highest_k = get_combinations_with_highest_k(satisfying_combinations)

               # for p in persons:
               #     print p


if __name__ == "__main__":
    main()
