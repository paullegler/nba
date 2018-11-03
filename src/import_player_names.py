import csv

output = "../files/players.txt"
path = "../excel/players.csv"
f2 = open(output, "a")

with open(path, "rb") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        line = line[0]
        number, name, position, age, team, games, games_started, minutes, fgm, \
            fga, fgp, threepm, threepa, threepp, twopm, twopa, twopp, \
            effective_fgp, ftm, fta, ftp, oreb, drb, trb, ast, stl, blk, tov, \
        pf, pts = line.split(',')
        name, id = name.split('\\')
        f2.write(name + "\n")

f2.close()
