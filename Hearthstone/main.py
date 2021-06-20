from BoardController import BoardController
from Board import Board
from Card import Card

if __name__ == "__main__":

	b1 = Board()
	b2 = Board()
	b1.add_card(Card(2,3),0)
	b1.add_card(Card(2,3),1)
	b1.add_card(Card(2,3),2)
	b1.add_card(Card(2,3),3)
	b2.add_card(Card(3,4),0)
	b2.add_card(Card(3,4),0)
	b2.add_card(Card(3,4),0)
	BC = BoardController(b1, b2)
	BC.simulate()