file = open("./data/input_day_1.txt", "r")
data = file.read()
parsedData = data.split("\n")
res = 0
numbers = {
  "one": '1',
  "two": '2',
  "three": '3',
  "four": '4',
  "five": '5',
  "six": '6',
  "seven": '7',
  "eight": '8',
  "nine": '9',
}
numLen = [3, 4, 5]

for word in parsedData: 
  i = 0
  j = len(word) - 1
  strNumber = ''
  while i < len(word):  
    if word[i].isnumeric():
      strNumber = word[i]
      break

    for length in numLen:
      if word[i:i + length] in numbers:
        strNumber = numbers[word[i:i + length]]
        break
    if len(strNumber) > 0:
      break
    i = i + 1

  while j >= i:
    if word[j].isnumeric():
      strNumber = strNumber + word[j]
      break
    for length in numLen:
      if word[j:j + length] in numbers:
        strNumber = strNumber + numbers[word[j:j + length]]
        break
    if len(strNumber) > 1:
      break
    j = j - 1
  
  res = res + int(strNumber)


print(res)

