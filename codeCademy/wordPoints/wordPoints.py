letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

zipped_letters = zip(letters, points)
letter_to_points = {key:value for key, value in zipped_letters}
letter_to_points[""] = 0
print(letter_to_points)

def score_word(word):
  point_total = 0

  for letter in word:
    # print("index", letter)
    point_total += letter_to_points.get(letter, 0)
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

players = ["player1", "wordNerd", "Lexi Con", "Prof Reader"]
words = [["BLUE", "TENNIS", "EXIT"], ["EARTH", "EYES", "MACHINE"], ["ERASER", "BELLY", "HUSKY"], ["ZAP", "COMA", "PERIOD"]]
zipped_players = zip(players, words)
player_to_words = {key:value for key, value in zipped_players}
print(player_to_words)
player_to_points = {}

for player in player_to_words:
  player_points = 0
  for word in player_to_words[player]:
    # print(word)
    player_points += score_word(word);
    player_to_points[player] = player_points
print(player_to_points)