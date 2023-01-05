def readFile():
  f = open('data.txt', 'r')
  Lines = f.readlines()
  
  return Lines


def chooseRucksacks(FileInput):
  totalCount = 0 
  for lines in FileInput:
    half = (int)(len(lines)/2)
    firstHalf = lines[0:half]
    secondHalf = lines[half:]
    
    letter = getMutualLetter(firstHalf, secondHalf)
    totalCount += getLetterValue(letter[0])
  
  return totalCount

def getMutualLetter(firstHalf, secondHalf):
  return list(set(firstHalf)&set(secondHalf))

def getLetterValue(letter):
  lista = [' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
  return lista[0].index(letter)

FileLines = readFile()
total = chooseRucksacks(FileLines)

print(total)