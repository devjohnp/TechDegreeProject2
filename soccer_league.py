import csv


def import_csv(filename):
    with open(filename, newline='') as csvfile:
        player_reader = csv.DictReader(csvfile, delimiter=',')
        players = list(player_reader)
    return players





if __name__ == '__main__':
    player_list = import_csv("soccer_players.csv")
    for player in player_list:
        print(player['Soccer Experience'])
