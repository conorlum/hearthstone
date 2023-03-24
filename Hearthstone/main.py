from hslog.parser import LogParser
from hslog.export import EntityTreeExporter

def main():
    parser = LogParser()
    with open("Power Logs\\202303141727Power.log") as f:
        parser.read(f)
    packet_tree = parser.games[0]
    exporter = EntityTreeExporter(packet_tree)
    export = exporter.export()

    player1 = game.players[0]
    player2 = game.players[1]

def get_current_minions(player):
    minions = []
    for e in player.entities:
        if e.tags[GameTag.CONTROLLER] == player.tags[GameTag.CONTROLLER] and e.zone == Zone.PLAY:
            if GameTag.CARDTYPE in e.tags.keys() and e.tags[GameTag.CARDTYPE] == CardType.MINION:
                minions.append(e)
    return minions

# You can then explore the attributes of the "export" object and the "game" object more precisely to fully understand how it works.
# I'm really not an expert but I hope it will help a little.

if __name__ == '__main__':
    main()
