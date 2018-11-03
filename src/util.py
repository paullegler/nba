
def get_teams():
    fname = '../files/team_abbrevs'

    with open(fname) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    abbrevs = {}
    for l in content:
        abbrev, team = l.split('\t')
        abbrevs[team] = abbrev
    return abbrevs
