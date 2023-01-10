def readFile():
  f = open('data.txt', 'r')
  Lines = f.readlines()
  
  return Lines


def chooseRucksacks(FileInput):
  totalCount = 0 
  #for lines in FileInput:
  for line in range(0, len(FileInput), 3):
    firstLine = (FileInput[line]).replace("\n",'')
    secondLine = FileInput[line+1]
    thirdLine = FileInput[line+2]
    
    letter = (getMutualLetter(firstLine, secondLine, thirdLine))

    totalCount += getLetterValue(letter[0])
  return totalCount

def getMutualLetter(firstLine, secondLine, thirdLine):
  return list(set(firstLine)&set(secondLine)&set(thirdLine))

def getLetterValue(letter):
  lista = [' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
  return lista[0].index(letter)

FileLines = readFile()
total = chooseRucksacks(FileLines)

print(total)