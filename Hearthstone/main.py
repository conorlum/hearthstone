import BoardController
import Board
import Card

if __name__ == "__main__":

	c23 = Card(2,3)
	c34 = Card(3,4)
	b1 = Board()
	b2 = Board()
	b1.add_card(c23,0)
	b2.add_card(c34,0)
	BC = BoardController(b1, b2)
	BC.simulate()