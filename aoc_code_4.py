from general_functions import read_data
import numpy as np

day = 4
data = read_data(day, test=False)

# part 1
drawn_numbers = [int(x) for x in data[0].split(',')]
bingo_cards = [x for x in data[1:] if x != '']
bingo_cards = [[int(y) for y in x.split(' ') if y != ''] for x in bingo_cards]

nr_of_cards = int(len(bingo_cards) / 5)

bingo_cards = np.array(bingo_cards).reshape(nr_of_cards, 5, 5)


def find_card(bingo_cards, drawn_numbers, find_first=True):
    card_counter = []
    bingo_cards_zero = np.zeros(bingo_cards.shape, dtype=int)
    for number in drawn_numbers:

        bingo_cards_zero = np.where(bingo_cards == number, 1, bingo_cards_zero)

        for card in range(bingo_cards.shape[0]):
            for row_or_col in range(bingo_cards.shape[1]):
                if np.sum(bingo_cards_zero[card, row_or_col]) == 5 or np.sum(
                        bingo_cards_zero[card, :, row_or_col]) == 5:
                    sum = np.sum(np.where(bingo_cards_zero[card] == 0, bingo_cards[card], 0))
                    if find_first == True:
                        return [card, number, sum]
                    else:
                        card_counter.append(card)
                        card_counter = list(set(card_counter))
                        if len(card_counter) == nr_of_cards:
                            return [card, number, sum]


result = find_card(bingo_cards, drawn_numbers, find_first=True)
print(result[1] * result[2])

# part 2
result = find_card(bingo_cards, drawn_numbers, find_first=False)
print(result[1] * result[2])
