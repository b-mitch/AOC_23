import os
import math
        
# PART 1

# # Helper function to build hand dictionaries
# def build_dict(hand):
#     output = dict()
#     i = 0
#     while i < len(hand):
#         val = hand[i]
#         if val not in output:
#             output[val] = 1
#         else:
#             output[val] += 1
#         i += 1
    
#     return output

# def has_2_pairs(values):
#     count = 0
#     for val in values:
#         if val == 2:
#             count += 1
#     if count == 2:
#         return True
#     return False

# def find_winner(hand1, hand2):
#     # Build dictionary for each hand with card count
#     hand1_dict = build_dict(hand1)
#     hand2_dict = build_dict(hand2)
#     # Determine the highest number of matches for each hand 
#     most_matches1 = max(hand1_dict.values())
#     most_matches2 = max(hand2_dict.values())
#     # If the hands have different most matches, return the winner
#     if most_matches1 != most_matches2:
#         return hand1 if most_matches1 > most_matches2 else hand2
#     # If they both have 3 matches as their hightest, check if one beats the other with a full house
#     if most_matches1 == 3:
#         has_pair1 = 2 in hand1_dict.values()
#         has_pair2 = 2 in hand2_dict.values()
#         if has_pair1 != has_pair2:
#             return hand1 if has_pair1 else hand2
#     # If highest for both is pairs then check if one has two pairs
#     if most_matches1 == 2:
#         has_2_pairs1 = has_2_pairs(hand1_dict.values())
#         has_2_pairs2 = has_2_pairs(hand2_dict.values())
#         if has_2_pairs1 != has_2_pairs2:
#             return hand1 if has_2_pairs1 else hand2
#     # If they're even in terms of hand strength, return whichever has the first highest card
#     alpha_order = ['T','J','Q','K','A']
#     i = 0
#     while i < len(hand1):
#         card1 = hand1[i]
#         card2 = hand2[i]
#         if card1 != card2:
#             # If they're both a digit, return the higher
#             if card1.isdigit() and card2.isdigit():
#                 return hand1 if card1 > card2 else hand2
#             # If one or the other is an alpha, return the hand with alpha
#             elif card1.isdigit():
#                 return hand2
#             elif card2.isdigit():
#                 return hand1
#             # If both are alpha, return the hand with the highest alpha
#             else:
#                 return hand1 if alpha_order.index(card1) > alpha_order.index(card2) else hand2
#         i += 1
#     # If hands are the same, return None
#     return None

# # Custom minheap class that sorts based on the hand and also stores the hand value
# class MinHeap:
#     def __init__(self):
#         self.data = []

#     def push(self, val):
#         self.data.append(val)
#         self.percolate_up()

#     def pop(self):
#         if self.size() == 0:
#             return None
#         if self.size() == 1:
#             return self.data.pop()
        
#         head = self.data[0]
#         self.data[0] = self.data.pop()
#         self.percolate_down()

#         return head

#     def percolate_up(self):
#         i = self.size() - 1
#         while i > 0:
#             current = self.data[i]
#             parent_i = (i - 1) // 2
#             parent = self.data[parent_i]
#             parent_hand = parent[0]
#             current_hand = current[0]
#             winner = find_winner(parent_hand, current_hand)
#             # print(parent_hand)
#             # print(current_hand)
#             # print(winner)
#             if winner == parent_hand:
#                 # print('this runs')
#                 self.swap(i, parent_i)
#                 i = parent_i
#             else:
#                 # print('\n')
#                 break

#     def percolate_down(self):
#         i = 0
#         while True:
#             left_i = i * 2 + 1
#             right_i = i * 2 + 2
#             left_child = self.data[left_i] if left_i < self.size() else None
#             right_child = self.data[right_i] if right_i < self.size() else None
#             current_hand = self.data[i][0]
#             left_hand = None
#             right_hand = None
#             if left_child is not None:
#                 left_hand = left_child[0]
#             if right_child is not None:
#                 right_hand = right_child[0]
#             if left_hand is None and right_hand is None:
#                 break
#             if (left_hand is None or find_winner(current_hand, left_hand) != current_hand) and (right_hand is None or find_winner(current_hand, right_hand) != current_hand):
#                 break
            
#             worst_child_index = None
#             if left_hand is not None and right_hand is not None:
#                 worst_child_index = left_i if find_winner(left_hand, right_hand) == right_hand else right_i
#             elif left_hand is None:
#                 worst_child_index = right_i
#             elif right_hand is None:
#                 worst_child_index = left_i

#             self.swap(i, worst_child_index)
#             i = worst_child_index

#     def swap(self, i1, i2):
#         val2 = self.data[i2]
#         self.data[i2] = self.data[i1]
#         self.data[i1] = val2

#     def size(self):
#         return len(self.data)

# def sum_winnings(hands):
#     total_winnings = 0
#     heap = MinHeap()
#     with open(hands, 'r') as file:
#         for line in file:
#             line = line.strip()
#             hand = ''
#             for i in range(5):
#                 hand += line[i]
#             bid = ''
#             i = 6
#             while i < len(line):
#                 bid += line[i]
#                 i += 1
#             bid = int(bid)
#             heap.push((hand, bid))
#     rank = 1
#     # print(heap.data)
#     while heap.size() > 0:
#         hand, bid = heap.pop()
#         # print(hand, bid * rank)
#         total_winnings += (rank * bid)
#         rank += 1

#     return total_winnings

# PART 2

# Helper function to build hand dictionaries
def build_dict(hand):
    output = dict()
    i = 0
    while i < len(hand):
        val = hand[i]
        if val not in output:
            output[val] = 1
        else:
            output[val] += 1
        i += 1
    # Account for Jokers by incrementing card with highest value for each Joker and decrement Jokers to 0
    if 'J' in output:
        joker_count = output['J']
        output['J'] = 0
        max_card = max(output, key=output.get)
        for i in range(joker_count):
            output[max_card] += 1
    return output

def has_2_pairs(values):
    count = 0
    for val in values:
        if val == 2:
            count += 1
    if count == 2:
        return True
    return False

def find_winner(hand1, hand2):
    # Build dictionary for each hand with card count
    hand1_dict = build_dict(hand1)
    hand2_dict = build_dict(hand2)
    # Determine the highest number of matches for each hand 
    most_matches1 = max(hand1_dict.values())
    most_matches2 = max(hand2_dict.values())
    # If the hands have different most matches, return the winner
    if most_matches1 != most_matches2:
        return hand1 if most_matches1 > most_matches2 else hand2
    # If they both have 3 matches as their hightest, check if one beats the other with a full house
    if most_matches1 == 3:
        has_pair1 = 2 in hand1_dict.values()
        has_pair2 = 2 in hand2_dict.values()
        if has_pair1 != has_pair2:
            return hand1 if has_pair1 else hand2
    # If highest for both is pairs then check if one has two pairs
    if most_matches1 == 2:
        has_2_pairs1 = has_2_pairs(hand1_dict.values())
        has_2_pairs2 = has_2_pairs(hand2_dict.values())
        if has_2_pairs1 != has_2_pairs2:
            return hand1 if has_2_pairs1 else hand2
    # If they're even in terms of hand strength, return whichever has the first highest card
    alpha_order = ['T','Q','K','A']
    i = 0
    while i < len(hand1):
        card1 = hand1[i]
        card2 = hand2[i]
        if card1 != card2:
            # If they're both a digit, return the higher
            if card1.isdigit() and card2.isdigit():
                return hand1 if card1 > card2 else hand2
            # If one or the other is an alpha (except J), return the hand with alpha
            elif card1.isdigit():
                if card2 == 'J':
                    return hand1
                return hand2
            elif card2.isdigit():
                if card1 == 'J':
                    return hand2
                return hand1
            # If both are alpha, return the hand with the highest alpha
            else:
                if card1 == 'J':
                    return hand2
                elif card2 == 'J':
                    return hand1
                else:
                    return hand1 if alpha_order.index(card1) > alpha_order.index(card2) else hand2
        i += 1
    # If hands are the same, return None
    return None

# Custom minheap class that sorts based on the hand and also stores the hand value
class MinHeap:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)
        self.percolate_up()

    def pop(self):
        if self.size() == 0:
            return None
        if self.size() == 1:
            return self.data.pop()
        
        head = self.data[0]
        self.data[0] = self.data.pop()
        self.percolate_down()

        return head

    def percolate_up(self):
        i = self.size() - 1
        while i > 0:
            current = self.data[i]
            parent_i = (i - 1) // 2
            parent = self.data[parent_i]
            parent_hand = parent[0]
            current_hand = current[0]
            winner = find_winner(parent_hand, current_hand)
            # print(parent_hand)
            # print(current_hand)
            # print(winner)
            if winner == parent_hand:
                # print('this runs')
                self.swap(i, parent_i)
                i = parent_i
            else:
                # print('\n')
                break

    def percolate_down(self):
        i = 0
        while True:
            left_i = i * 2 + 1
            right_i = i * 2 + 2
            left_child = self.data[left_i] if left_i < self.size() else None
            right_child = self.data[right_i] if right_i < self.size() else None
            current_hand = self.data[i][0]
            left_hand = None
            right_hand = None
            if left_child is not None:
                left_hand = left_child[0]
            if right_child is not None:
                right_hand = right_child[0]
            if left_hand is None and right_hand is None:
                break
            if (left_hand is None or find_winner(current_hand, left_hand) != current_hand) and (right_hand is None or find_winner(current_hand, right_hand) != current_hand):
                break
            
            worst_child_index = None
            if left_hand is not None and right_hand is not None:
                worst_child_index = left_i if find_winner(left_hand, right_hand) == right_hand else right_i
            elif left_hand is None:
                worst_child_index = right_i
            elif right_hand is None:
                worst_child_index = left_i

            self.swap(i, worst_child_index)
            i = worst_child_index

    def swap(self, i1, i2):
        val2 = self.data[i2]
        self.data[i2] = self.data[i1]
        self.data[i1] = val2

    def size(self):
        return len(self.data)

def sum_winnings(hands):
    total_winnings = 0
    heap = MinHeap()
    with open(hands, 'r') as file:
        for line in file:
            line = line.strip()
            hand = ''
            for i in range(5):
                hand += line[i]
            bid = ''
            i = 6
            while i < len(line):
                bid += line[i]
                i += 1
            bid = int(bid)
            heap.push((hand, bid))
    rank = 1
    # print(heap.data)
    while heap.size() > 0:
        hand, bid = heap.pop()
        # print(hand, bid * rank)
        total_winnings += (rank * bid)
        rank += 1

    return total_winnings

# TESTS

# heap = MinHeap()
# heap.push(('32T3K', 765))
# heap.push(('T55J5', 684))
# heap.push(('KK677', 28))
# heap.push(('KTJJT', 220))
# heap.push(('QQQJA', 483))
# print(heap.data)
# print(heap.pop())

puzzle_input = os.path.join(os.path.dirname(__file__), 'puzzleinput.txt')
 
# print(find_winner('3JJ12', 'J1252'))

print(sum_winnings(puzzle_input))
