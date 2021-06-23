from BoardController import BoardController
from Board import Board
from Card import Card

if __name__ == "__main__":

	b1 = Board()
	b2 = Board()
	b1.add_card(Card(2000,1000),0)
	b2.add_card(Card(1,1, poisonous = True),0)
	b2.add_card(Card(1,1, poisonous = True),1)
	BC = BoardController(b1, b2)
	BC.big_simulate()