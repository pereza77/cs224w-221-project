import numpy as np
import matplotlib.pyplot as plt
import re

# change file name, 
# add special cases for any funny accents
# bc matplotlib doesn't like them.

# usage: python plot_games_by_pos.py

N = 16
ind = np.arange(N)
width = 0.35

filename = "games_by_pos/RealMadrid_games_by_pos.txt"
games_by_pos = open(filename, "r")

team1 = ""
team2 = ""

team1Means = []
team2Means = []

hasPos = False
for i, line in enumerate(games_by_pos):
	if "Position" in line:
		_, team1, team2 = re.split(r'\s{2,}', line.rstrip())
		hasPos = True
		continue
	
	if line == "\n":
		hasPos = False

		# plot!
		
		fig, ax = plt.subplots()
		rects1 = ax.bar(ind, tuple(team1Means), width, color='r')
		rects2 = ax.bar(ind+width, tuple(team2Means), width, color='y')
		ax.set_ylabel('Weight of passes')
		ax.set_title('Weight of passes by team')
		ax.set_xticks(ind + width)
		ax.set_xticklabels(('GK-GK', 'GK-STR', 'GK-DEF', 'GK-MID',\
			'STR-GK', 'STR-STR', 'STR-DEF', 'STR-MID', \
			'DEF-GK', 'DEF-STR', 'DEF-DEF', 'DEF-MID', \
			'MID-GK', 'MID-STR', 'MID-DEF', 'MID-MID'))


		# if "Club" in team1:
		# 	team1 = "Club Atletico de Madrid"

		if "Bayern" in team1:
			team1 = "FC Bayern Munchen"

		if "Bayern" in team2:
			team2 = "FC Bayern Munchen"

		if "FF" in team2:
			team2 = "Malmo FF"

		ax.legend((rects1[0], rects2[0]), (team1, team2))

		plt.show()

		team1Means = []
		team2Means = []

	if hasPos:
		pos, num1, num2 = re.split(r'\s{2,}', line.rstrip())
		team1Means.append(int(num1))
		team2Means.append(int(num2))


# print out last set
fig, ax = plt.subplots()

rects1 = ax.bar(ind, tuple(team1Means), width, color='r')
rects2 = ax.bar(ind+width, tuple(team2Means), width, color='y')
ax.set_ylabel('Weight of passes')
ax.set_title('Weight of passes by team')
ax.set_xticks(ind + width)
ax.set_xticklabels(('GK-GK', 'GK-STR', 'GK-DEF', 'GK-MID',\
	'STR-GK', 'STR-STR', 'STR-DEF', 'STR-MID', \
	'DEF-GK', 'DEF-STR', 'DEF-DEF', 'DEF-MID', \
	'MID-GK', 'MID-STR', 'MID-DEF', 'MID-MID'))

if "Bayern" in team2:
	team2 = "FC Bayern Munchen"

ax.legend((rects1[0], rects2[0]), (team1, team2))

plt.show()

team1Means = []
team2Means = []

