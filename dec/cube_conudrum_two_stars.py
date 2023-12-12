def main():
  file = open("./data/input_day_2.txt", "r")
  data = file.read()
  games = data.split("\n")
  result = 0
  
  for game in games:
    gameInfo = game.split(":")
    sets = gameInfo[1].split(";")
    balls = minAmountOfBalls(sets)
    pow = balls["r"] * balls["g"] * balls["b"]
    result = result + pow
  
  print(result)

def minAmountOfBalls(sets):
  balls = {
    "r": 0,
    "g": 0,
    "b": 0
  }

  for set in sets:
    setArray = set.split(",")
    for ball in setArray:
      attributes = ball.split(" ")
      balls[attributes[2][0]] = max(balls[attributes[2][0]], int(attributes[1]))

  return balls



  

main()