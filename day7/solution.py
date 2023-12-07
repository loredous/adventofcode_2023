from dataclasses import dataclass
from enum import Enum
from functools import cmp_to_key

class HandType(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

PART1_CARD_INDEX = 'AKQJT98765432'
PART2_CARD_INDEX = 'AKQT98765432J'

@dataclass
class Hand:
    cards: str
    bet: int

class Part1Hand(Hand):

    def __lt__(self, other):
        return part1_hand_comparator(other.cards, self.cards)
    
    def __gt__(self, other):
        return part1_hand_comparator(self.cards, other.cards)
    
    def __eq__(self, other):
        return part1_hand_comparator(self.cards, other.cards) is None

def part1_hand_classifier(hand) -> HandType:
    parsed_hand = {}
    for card in hand:
        if card not in parsed_hand:
            parsed_hand[card] = 1
        else:
            parsed_hand[card] += 1
    if len(parsed_hand) == 1:
        return HandType.FIVE_OF_A_KIND
    if len(parsed_hand) == 2:
        if 4 in parsed_hand.values():
            return HandType.FOUR_OF_A_KIND
        else:
            return HandType.FULL_HOUSE
    if len(parsed_hand) == 3:
        if 3 in parsed_hand.values():
            return HandType.THREE_OF_A_KIND
        else:
            return HandType.TWO_PAIR
    if 2 in parsed_hand.values():
        return HandType.ONE_PAIR
    return HandType.HIGH_CARD

def part1_hand_comparator(hand1, hand2) -> bool:
    hand1_type = part1_hand_classifier(hand1)
    hand2_type = part1_hand_classifier(hand2)
    if hand1_type.value > hand2_type.value:
        return True
    elif hand1_type.value < hand2_type.value:
        return False
    else:
        for card1, card2 in zip(hand1, hand2):
            if PART1_CARD_INDEX.index(card1) < PART1_CARD_INDEX.index(card2):
                return True
            elif PART1_CARD_INDEX.index(card1) > PART1_CARD_INDEX.index(card2):
                return False
    return None

class Part2Hand(Hand):

    def __lt__(self, other):
        return part2_hand_comparator(other.cards, self.cards)
    
    def __gt__(self, other):
        return part2_hand_comparator(self.cards, other.cards)
    
    def __eq__(self, other):
        return part2_hand_comparator(self.cards, other.cards) is None

def part2_hand_classifier(hand) -> HandType:
    parsed_hand = {}
    for card in hand:
        if card not in parsed_hand:
            parsed_hand[card] = 1
        else:
            parsed_hand[card] += 1
    if len(parsed_hand) == 1:
        return HandType.FIVE_OF_A_KIND
    if len(parsed_hand) == 2:
        if "J" in parsed_hand.keys():
            return HandType.FIVE_OF_A_KIND
        if 4 in parsed_hand.values():
            return HandType.FOUR_OF_A_KIND
        else:
            return HandType.FULL_HOUSE
    if len(parsed_hand) == 3:
        if 3 in parsed_hand.values():
            if "J" in parsed_hand.keys():
                return HandType.FOUR_OF_A_KIND
            else:
                return HandType.THREE_OF_A_KIND
        else:
            if "J" in parsed_hand.keys():
                if parsed_hand["J"] == 2:
                    return HandType.FOUR_OF_A_KIND
                else:
                    return HandType.FULL_HOUSE
            else:
                return HandType.TWO_PAIR
    if len(parsed_hand) == 4:
        if "J" in parsed_hand.keys():
            return HandType.THREE_OF_A_KIND
        else:
            return HandType.ONE_PAIR
    if "J" in parsed_hand.keys():
        return HandType.ONE_PAIR
    return HandType.HIGH_CARD

def part2_hand_comparator(hand1, hand2) -> bool:
    hand1_type = part2_hand_classifier(hand1)
    hand2_type = part2_hand_classifier(hand2)
    if hand1_type.value > hand2_type.value:
        return True
    elif hand1_type.value < hand2_type.value:
        return False
    else:
        for card1, card2 in zip(hand1, hand2):
            if PART2_CARD_INDEX.index(card1) < PART2_CARD_INDEX.index(card2):
                return True
            elif PART2_CARD_INDEX.index(card1) > PART2_CARD_INDEX.index(card2):
                return False
    return None
 

if __name__ == '__main__':
    hands = []
    with open('day7/input') as f:
        for line in f:
            hands.append(Hand(line[:5], int(line.strip()[5:])))
    
    # Part 1
    hands.sort(key=lambda x: Part1Hand(x.cards, x.bet))
    total = 0
    for index, hand in enumerate(hands):
        total += hand.bet * (index+1)
    print(total)

    # Part 2
    hands.sort(key=lambda x: Part2Hand(x.cards, x.bet))
    total = 0
    for index, hand in enumerate(hands):
        total += hand.bet * (index+1)
    print(total)