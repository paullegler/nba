class Player:
    '''
    These are averages
    '''
    def __init__(self, id, name, fga, fgm, fta, ftm, threem, rebounds, assists, \
        steals, blocks, turnovers, points, games, team):
        self.id = id
        self.name = name
        self.fga = float(fga)
        self.fgm = float(fgm)
        self.fta = float(fta)
        self.ftm = float(ftm)
        self.threem = int(threem)
        self.rebounds = int(rebounds)
        self.assists = int(assists)
        self.steals = int(steals)
        self.blocks = int(blocks)
        self.turnovers = int(turnovers)
        self.points = int(points)
        self.games = int(games)
        self.team = team
        if self.fga > 0: fgp = self.fgm/self.fga
        else: fgp = 0.0
        if self.fta > 0: ftp = self.ftm/self.fta
        else: ftp = 0.0
        self.fantasy_order = [fgp, ftp, self.threem, \
         self.rebounds, self.assists, self.steals, self.blocks, self.turnovers, \
         self.points]

    '''
    Calculate the number of stats generated in the next x number of games
    '''
    def totalsForNextGames(self, number):
        totals = [self.threem, self.rebounds, self.assists, self.steals, \
            self.blocks, self.turnovers, self.points]
        return [i *  number for i in totals]

    '''
    Calculate value a player has given a weighting system
    '''
    def value(self, weights):
        total = 0
        for i in range(len(weights)):
            total += weights[i] * self.fantasy_order[i]
        return total
