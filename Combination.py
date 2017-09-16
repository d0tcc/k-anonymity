class Combination():
    def __init__(self, iAge, iZip, iSex, k, grouped_persons):
        self.iAge = iAge
        self.iZip = iZip
        self.iSex = iSex
        self.k = k
        self.grouped_persons = grouped_persons

    def __str__(self):
        txt = "----------------------------------------------------------------\n"
        txt += "Age: {0}, ZIP: {1}, Sex: {2}, k: {3}\n".format(self.iAge, self.iZip, self.iSex, self.k)
        i = 1
        for group in self.grouped_persons:
            txt += "--------\n"
            txt += "Group: " + str(i) + "\n"
            txt += "--------\n"
            i = i + 1
            for p in self.grouped_persons[group]:
                txt += str(p) + "\n"
            txt += "\n"
        return txt + "\n"


    def get_steps(self):
        return self.iAge + self.iZip + self.iSex