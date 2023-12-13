import os
# PART 1

# def get_score(scratchers):
#     total_score = 0
#     with open(scratchers, 'r') as file:
#         for card in file:
#             winning_numbers = []
#             your_numbers = []
#             i = 10
#             card = card.strip()
#             while i < len(card):
#                 number = ''
#                 if card[i].isdigit():
#                     while i < len(card) and card[i].isdigit():
#                         number += card[i]
#                         i += 1
#                     if i < 40:
#                         winning_numbers.append(number)
#                     else:
#                         your_numbers.append(number)
#                 i += 1
#             card_score = 0
#             for numb in your_numbers:
#                 if numb in winning_numbers:
#                     if card_score == 0:
#                         card_score = 1
#                     else:
#                         card_score *= 2
#             total_score += card_score
        
#     return total_score

# PART 2

def get_score(scratchers):
    with open(scratchers, 'r') as file:
        card_copies = {}
        card = 1
        for line in file:
            # Add card to card copies if not already there
            if card not in card_copies:
                card_copies[card] = 1
            winning_numbers = []
            your_numbers = [] 
            # use for puzzle input
            i = 10
            # use for sample
            # i = 5
            line = line.strip()
            # Add numbers to winning numbers or your numbers depending on index
            while i < len(line):
                number = ''
                if line[i].isdigit():
                    while i < len(line) and line[i].isdigit():
                        number += line[i]
                        i += 1
                    # use for puzzle input
                    if i < 40:
                    # use for sample
                    # if i < 23:
                        winning_numbers.append(number)
                    else:
                        your_numbers.append(number)
                i += 1
            wins = 0
            # Iterate your numbers
            for numb in your_numbers:
                if numb in winning_numbers:
                    wins += 1
                    card_won = card + wins
                    # Increment the count of each card won for each copy of current card
                    if card_won in card_copies:
                        card_copies[card_won] += card_copies[card]
                    else:
                        card_copies[card_won] = card_copies[card] + 1
            card += 1
    return sum(card_copies.values())

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'puzzleinput.txt')

# for i, char in enumerate('Card   1:  5 27 94 20 50  7 98 41 67 34 | 34  9 20 90  7 77 44 71 27 12 98  1 79 96 24 51 25 84 67 41  5 13 78 31 26'):
#     if char == '|':
#         print(i)
#         break

print(get_score(puzzle_input))
