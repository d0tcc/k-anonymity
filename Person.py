class Person():
	def __init__(self, name, age, sex, zipcode, illness):
		self.name = name
		self.age = age
		self.sex = sex
		self.zipcode = zipcode
		self.illness = illness

	def __str__(self):
		return "{0}, {1}, {2}, {3}, {4}".format(self.name, self.age, self.sex, self.zipcode, self.illness)