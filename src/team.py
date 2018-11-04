import player
import read_players
import read_schedule

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add(self, players):
        for p in players:
            self.players.append(p)

    def averages(self, team_games_played=None):
        totals = [0.0] * 9
        for player in self.players:
            avg = player.averages()
            for i in range(len(totals)):
                if team_games_played != None:
                    totals[i] += avg[i] * team_games_played[player.team]
                else:
                    totals[i] += avg[i]
        return totals

    def totalsForRange(self, start_day, start_month, start_year, end_day, end_month, end_year):
        read_schedule.output(start_day, start_month, start_year, end_day, end_month, end_year)
        team_games_played = read_schedule.read_schedule_file()
        return self.averages(team_games_played)

def add_names_from_team_file(team_name, names):
    fname = "../files/" + team_name
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    for name in content:
        names.add(name)
    return names

def main():
    team_name = "paul"
    opp_name = "nick"
    team = Team(team_name)
    opp = Team(opp_name)

    names = set()
    opp_names = set()
    names = add_names_from_team_file(team_name, names)
    opp_names = add_names_from_team_file(opp_name, opp_names)

    players = read_players.find_players(names)
    team.add(players)
    avg = team.averages()
    print [i / 13.0 for i in avg]


    opp_players = read_players.find_players(opp_names)
    opp.add(opp_players)
    opp_avg = team.averages()
    print [i / 12.0 for i in opp_avg]


    #print [i / 13.0 for i in avg]
    print opp.totalsForRange(11, 4, 2018, 11, 11, 2018)
    print team.totalsForRange(11, 4, 2018, 11, 11, 2018)


if __name__ == '__main__':
    main()
