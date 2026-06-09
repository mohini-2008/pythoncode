players = [
    (1, "Virat", 98),
    (2, "Rohit", 100),
    (3, "Vaibhav", 99),
    (4, "Mahi", 101)
]

# 1. Max score player
max_player = players[0]

for p in players:
    if p[2] > max_player[2]:
        max_player = p

print("Max Score Player =", max_player[1])

# 2. Total score
total = 0
for p in players:
    total = total + p[2]

print("Total Score =", total)

# 3. Top 3 players
players = sorted(players, reverse=True)

print("Top 3 Players:")
for i in range(3):
    print(players[i][1], players[i][2])
