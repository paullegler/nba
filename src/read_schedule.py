import csv
from operator import itemgetter



days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

class Date:
    def __init__(self, day, month, year):
        self.month = int(month)
        self.day = int(day)
        self.year = int(year)

    def __eq__(self, other):
        return self.month == other.month and self.year == other.year and self.day == other.day

    def __hash__(self):
        return hash((self.month, self.day, self.year))

    def __repr__(self):
        return str((self.day, self.month, self.year))

    def __lt__(self, other):
        if self.year > other.year:
            return False
        if self.year < other.year:
            return True
        if self.month > other.month:
            return False
        if self.month < other.month:
            return True
        return self.day < other.day

    def next(self):
        if self.day < days_in_month[self.month]:
            return Date(self.day + 1, self.month, self.year)
        if self.month < 12:
            return Date(1, self.month + 1, self.year)
        return Date(1, 1, self.year + 1)

class Year:
    def __init__(self):
        self.dates = {} # map date object: list of teams

    def add(self, date, teams):
        if date in self.dates:
            self.dates[date].extend(teams)
        else:
            self.dates[date] = teams

    def quantity(self, start, end):
        teams = {}
        current_day = start
        while current_day < end:
            if current_day in self.dates:
                for t in self.dates[current_day]:
                    if t in teams:
                        teams[t] += 1
                    else:
                        teams[t] = 1
            current_day = current_day.next()
        return teams

y = Year()

path = "../excel/schedule.csv"

with open(path, "rb") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        if i == 0: continue

        line = line[0]
        round, date, location, home, away, result = line.split(',')

        mdy, time = date.split(' ')

        day, month, year = mdy.split('/')
        d = Date(day, month, year)

        if home == 'LA Clippers': home = 'Los Angeles Clippers'
        if away == 'LA Clippers': away = 'Los Angeles Clippers'
        y.add(d, [home, away])


while True:
    start_day, start_month, start_year = raw_input("Start date in format: day month year ").split(' ')
    end_day, end_month, end_year = raw_input("End date (exclusive) in format: day month year ").split(' ')
    start_date = Date(start_day, start_month, start_year)
    end_date = Date(end_day, end_month, end_year)

    teams = y.quantity(start_date, end_date)
    sorted_teams = sorted(teams.iteritems(), key=itemgetter(1), reverse=True)

    fname = '../files/teams_games_played'
    open(fname, 'w').close()

    f = open(fname, 'a')
    for team in sorted_teams:
        f.write(str(team) + '\n')
    f.close()
