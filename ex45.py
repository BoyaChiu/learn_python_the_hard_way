##Animal is-a object(yes,sort of confusing )look at the extra credit
class Animal(object):
	pass

##??
class Dog(Animal):
	def __init__(self,name):
		##??
		self.name=name

##??
class Cat(Animal):
	
	def __intit__(self,name):
	##??
	self.name=name
##??
class Person(object):
	
	def __init__(self,name):
	##??
	self.name=name

	##Person has a-s pet of some kind
	self.pet=None

##??
class Employee(Person):
	
	def __init__(self,name,salary):

		##?? hmm waht is this strange magic?
		super(Employee,self) __init__(same)
		##??
		self.salary=salary

##??
class Fish(object):
	pass

##??
class Halibut(Fish):
	pass


##rover is-a Dog
rover=Dog("Rover")

##??
Satan=Cat("Satan")

##??
mary=Person("Mary")

##??
mary.pet=satan

##??
frank=Employee("Frank",120000)

##??
frank.pet=rover


##??
flipper=Fish()

##??
crouse=Salman()

##??
harry=Halibut()