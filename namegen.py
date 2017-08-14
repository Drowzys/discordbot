import random


def generateName(infile):
	with open(infile) as f:
		nameContents = f.read()
	lines = nameContents.splitlines()
	line_number = random.randrange(0, len(lines))
	return lines[line_number]





def generateRace(infile):
	with open(infile) as f:
		raceContents = f.read()
	lines = raceContents.splitlines()
	line_number = random.randrange(0, len(lines))
	return lines[line_number]


def generateAge(infile):
	with open(infile) as f:
		ageContents = f.read()
	lines = ageContents.splitlines()
	line_number = random.randrange(0, len(lines))
	return lines[line_number]


def generateCharecteristic(infile):
	with open(infile) as f:
		charContents = f.read()
	lines = charContents.splitlines()
	line_number = random.randrange(0, len(lines))
	return lines[line_number]
 



def char():
	return generateCharecteristic("char.txt")
def age():
	return generateAge("age.txt")
def race():
	return generateRace("races.txt")
def name():
	return generateName("names.txt")

name()
age()
race()		
char()
	