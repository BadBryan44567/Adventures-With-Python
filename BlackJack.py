def value_of_card(card: str):
	if card in "JQK":
		return 10
	elif card == 'A':
		return 1
	else:
		return int(card)

def higher_card(card1: str, card2: str):
	value_one = value_of_card(card1)
	value_two = value_of_card(card2)
	
	if value_one > value_two:
		return card1
	if value_two > value_one:
		return card2
	return card1, card2

def value_of_ace(card1, card2):
	value_one = value_of_card(card1)
	value_two = value_of_card(card2)
	total_value = value_one + value_two
	ace_value1 = 1
	ace_value2 = 11

	if card1 == 'A' or card2 == 'A' or total_value + ace_value2 <= 21:
		return ace_value2
	else:
		return ace_value1

def is_blackjack(card1, card2):
	value_one = value_of_card(card1)
	value_two = value_of_card(card2)
	total_value = value_one + value_two

	if card1 == 'A' and card2 in "JQK" or total_value >= 21:
		return True
	else:
		return False
	
def can_split_pairs(card1, card2):
	value_one = value_of_card(card1)
	value_two = value_of_card(card2)

	if value_one == value_two:
		return True
	return False

def can_double_down(card1, card2):
	value_one = value_of_card(card1)
	value_two = value_of_card(card2)
	total_value = value_one + value_two

	if total_value >= 9 and total_value <= 11:
		return True
	return False

print(
	value_of_card("K"),
	value_of_card("4"),
	value_of_card("A"),

	higher_card("K", "10"),
	higher_card("4", "6"),
	higher_card("K", "A"),

	value_of_ace("6", "K"),
	value_of_ace("7", "3"),

	is_blackjack("A", "K"),
	is_blackjack("10", "9"),

	can_split_pairs("Q", "K"),
	can_split_pairs("10", "A"),

	can_double_down("A", "9"),
	can_double_down("10", "2")
)

