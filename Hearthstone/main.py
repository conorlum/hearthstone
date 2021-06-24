from BoardController import BoardController
from Board import Board
from Card import Card

if __name__ == "__main__":

	b1 = Board()
	b2 = Board()
	b1.add_card(Card(2,1, reborn = True),0)
	b1.add_card(Card(1,1),1)
	b2.add_card(Card(1,1),0)
	b2.add_card(Card(1,1),2)
	b2.add_card(Card(1,1),1)
	BC = BoardController(b1, b2)
	BC.simulate()
	BC.board_states()