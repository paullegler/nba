import csv
import player
import util
from operator import itemgetter

# import read_schedule

path = "../excel/BBM_PlayerRankings"
'''
get zscores
'''
path = "../excel/players.csv"

teams_abbrevs = util.get_teams()
players = []
names = set()

def main():
    with open(path, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            line = line[0]
            number, name, position, age, team, games, games_started, minutes, fgm, \
                fga, fgp, threepm, threepa, threepp, twopm, twopa, twopp, \
                effective_fgp, ftm, fta, ftp, oreb, drb, trb, ast, stl, blk, tov, \
            pf, pts = line.split(',')


            name, id = name.split('\\')

            p = player.Player(id, name, fga, fgm, fta, ftm, threepm, trb, \
                ast, stl, blk, tov, pts, games, team)
            players.append(p)
            names.add(p.name)

    '''
    Read Free Agents
    '''
    free_agents = []
    fname = "../files/free_agents.txt"
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    for name in content:
        free_agents.append(name)

    '''
    Read how many games each time plays, generated by read_schedule.py
    '''
    team_games_played = {} # abbrev: number
    fname = '../files/teams_games_played'
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    for l in content:
         team, gp = eval(l)
         abbrev = teams_abbrevs[team]
         team_games_played[abbrev] = gp



    '''
    Grab user weights for each category
    '''
    # fgw, ftw, threew, rebw, astw, stlw, blkw, tovw, ptsw \
    #  = raw_input("Enter weighting system, " \
    #  + "values 1 to 100 based with 100 being very imporant \n" \
    #  + "fgp ftp 3pm reb ast stl blk tov pts :").split(' ')


    '''
    Hard wiring a weighting scheme here
    '''
    fgw, ftw, threew, rebw, astw, stlw, blkw, tovw, ptsw = \
     0, 0, 2, 1, 1, 3, 3, -1, 1

    values = {}
    for p in players:
        team = p.team
        games_played = 0
        if p.team in team_games_played:
            games_played = team_games_played[p.team]
        value = p.value([fgw, ftw, threew, rebw, astw, stlw, blkw, tovw, ptsw])
        values[p] = value * games_played

    sorted_players = sorted(values.iteritems(), key=itemgetter(1), reverse=True)
    for p in sorted_players:
        if p[0].name in free_agents:
            print p[0].name, p[1]

if __name__ == '__main__':
    main()
