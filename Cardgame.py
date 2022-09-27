def get_rounds(round):
	return [round, round+1, round+2]

def concatenate_rounds(rounds1, rounds2):
	return rounds1 + rounds2

def list_cointains_round(rounds, round):
	return round in rounds

def card_average(cards):
	return sum(cards) / len(cards)

def approx_average_is_average(cards):
	avg = card_average(cards)
	return (cards[0] + cards[-1]) / 2 == avg or cards[len(cards) // 2] == avg

def average_even_is_average_odd(cards):
	return card_average(cards[::2]) == card_average(cards[1 :: 2])

def maybe_double_last(cards: list):
	if cards[-1] == 11:
		new_value = cards[-1] * 2
		cards.remove(cards[-1])
		cards.append(new_value)
		return cards
	return cards

print(get_rounds(27))
print(concatenate_rounds([27,28,29], [34,35]))
print(list_cointains_round([27,28,29,24], 29))
print(list_cointains_round([27,28,29,26], 30))
print(card_average([5,6,7]))
print(approx_average_is_average([1,2,3]))
print(approx_average_is_average([1,2,3,5,9]))
print(average_even_is_average_odd([1,2,3,4]))
print(maybe_double_last([5,10,11]))