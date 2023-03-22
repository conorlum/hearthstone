from PowerParser import PowerParser

def main():
    parser = PowerParser()
    board_states = parser.boardParse("Power Logs/202303141727Power.log")
    print(board_states)
    for state in board_states:
        print(f"Turn {state['turn']}:")
        print("Enemy board:")
        for minion in state["enemy_board"]:
            print(f"\t{minion['name']} - Attack: {minion['attack']} - Health: {minion['health']}")
        print("Player board:")
        for minion in state["player_board"]:
            print(f"\t{minion['name']} - Attack: {minion['attack']} - Health: {minion['health']}")

if __name__ == '__main__':
    main()
