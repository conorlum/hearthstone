import re

class PowerParser:
    def __init__(self):
        self.turn_num = 0
        self.board_states = []

    def boardParse(self, log_file):
        self.turn_num = 0
        self.board_states = []

        with open(log_file, "r") as f:
            for line in f:
                if "BLOCK_START BlockType=TRIGGER Entity=" in line and "BlockType=TRIGGER Entity=GameEntity" not in line:
                    # print(line)
                    self.turn_num += 1
                    board_state = {"turn": self.turn_num, "enemy_board": [], "player_board": []}

                # Enemy board state
                if "FULL_ENTITY - Updating" in line and "cardId=" in line and "playerId=1" in line:
                    match = re.search(r"id=(\d+).*zone=(\w+).*cardId=(\w+).*attack=(\d+).*health=(\d+)", line)
                    if match:
                        entity_id = match.group(1)
                        zone = match.group(2)
                        card_id = match.group(3)
                        attack = match.group(4)
                        health = match.group(5)
                        board_state["enemy_board"].append({"entity_id": entity_id, "name": card_id, "attack": attack, "health": health})

                # Player board state
                if "FULL_ENTITY - Updating" in line and "cardId=" in line and "playerId=2" in line:
                    match = re.search(r"id=(\d+).*zone=(\w+).*cardId=(\w+).*attack=(\d+).*health=(\d+)", line)
                    if match:
                        entity_id = match.group(1)
                        zone = match.group(2)
                        card_id = match.group(3)
                        attack = match.group(4)
                        health = match.group(5)
                        board_state["player_board"].append({"entity_id": entity_id, "name": card_id, "attack": attack, "health": health})

                if "BLOCK_END" in line:
                    # print(line)
                    self.board_states.append(board_state)

        return self.board_states
