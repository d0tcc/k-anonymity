class Combination():
    def __init__(self, iAge, iZip, iSex, k):
        self.iAge = iAge
        self.iZip = iZip
        self.iSex = iSex
        self.k = k

    def __str__(self):
        return "a: {0}, z: {1}, s: {2}, k: {3}".format(self.iAge, self.iZip, self.iSex, self.k)


    def get_steps(self):
        return self.iAge + self.iZip + self.iSex