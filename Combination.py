class Combination():
    def __init__(self, iDate, iZip, iSex, k, grouped_persons):
        self.iDate = iDate
        self.iZip = iZip
        self.iSex = iSex
        self.k = k
        self.grouped_persons = grouped_persons

    def __str__(self):
        txt = "----------------------------------------------------------------\n"
        txt += "Date: {0}, ZIP: {1}, Sex: {2}, k: {3}, anon-score: {4}\n".format(self.iDate, self.iZip, self.iSex, self.k, self.get_anonymization_score())
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


    def get_anonymization_score(self):
        return self.iDate*(1.0/7.0) + self.iZip*(1.0/6.0) + self.iSex*(1.0/2.0)