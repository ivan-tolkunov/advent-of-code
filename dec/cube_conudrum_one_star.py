def main():
  file = open("./data/input_day_2.txt", "r")
  data = file.read()
  games = data.split("\n")
  result = 0
  rule = {
    "r": 12,
    "g": 13,
    "b": 14
  }
  
  for game in games:
    gameInfo = game.split(":")
    if isValidGame(gameInfo[1], rule):
      gameId = int(gameInfo[0].split(" ")[1])
      result = result + gameId

  
  print(result)

def isValidGame(sets, rule):
  setsArray = sets.split(";")
  for set in setsArray:
    balls = set.split(",")
    for ball in balls:
      attributes = ball.split(" ")
      amount = int(attributes[1])
      color = attributes[2][0]
      if amount > rule[color]:
        return False
      
  return True

main()