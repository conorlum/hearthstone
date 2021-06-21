from BoardController import BoardController
from Board import Board
from Card import Card

if __name__ == "__main__":

	b1 = Board()
	b2 = Board()
	b1.add_card(Card(2,1),0)
	b1.add_card(Card(1,3),1)
	b1.add_card(Card(2,1),2)
	b1.add_card(Card(1,3),1)
	b1.add_card(Card(2,1),3)
	b1.add_card(Card(1,3),4)
	b2.add_card(Card(1,1),0)
	b2.add_card(Card(3,2),1)
	b2.add_card(Card(1,1),2)
	b2.add_card(Card(3,2),3)
	b2.add_card(Card(1,1),4)
	b2.add_card(Card(3,2),5)
	BC = BoardController(b1, b2)
	BC.big_simulate()