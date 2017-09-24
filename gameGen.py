import random

def generateGame(infile):
	with open(infile) as f:
		nameContents = f.read()
	lines = nameContents.splitlines()
	line_number = random.randrange(0, len(lines))
	return lines[line_number]



def games():
	return generateGame("games.txt")


games()

