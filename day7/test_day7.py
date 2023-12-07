from day7.solution import part1_hand_classifier, HandType, part1_hand_comparator, part2_hand_classifier, part2_hand_comparator
from pytest import mark


@mark.parametrize('hand, expected_hand_type', [
    ['32T3K', HandType.ONE_PAIR],
    ['T55J5', HandType.THREE_OF_A_KIND],
    ['KK677', HandType.TWO_PAIR],
    ['KTJJT', HandType.TWO_PAIR],
    ['QQQJA', HandType.THREE_OF_A_KIND],
    ['KKKKK', HandType.FIVE_OF_A_KIND],
    ['KKKKQ', HandType.FOUR_OF_A_KIND],
    ['KKKQQ', HandType.FULL_HOUSE],
    ['12345', HandType.HIGH_CARD],
])
def test_part1_hand_classifier(hand, expected_hand_type):
    assert part1_hand_classifier(hand) == expected_hand_type

@mark.parametrize('hand1, hand2, expected_result', [
    ['32T3K', 'T55J5', False],
    ['T55J5', '32T3K', True],
    ['KKKKK', 'QQQQQ', True],
    ['KKKKQ', 'KKKKJ', True],
    ['KKKKK', 'KKKKK', None],
])
def test_part1_hand_comparator(hand1, hand2, expected_result):
    assert part1_hand_comparator(hand1, hand2) == expected_result

@mark.parametrize('hand, expected_hand_type', [
    ['23456', HandType.HIGH_CARD],
    ['2345J', HandType.ONE_PAIR],
    ['23455', HandType.ONE_PAIR],
    ['23355', HandType.TWO_PAIR],
    ['23J55', HandType.THREE_OF_A_KIND],
    ['23555', HandType.THREE_OF_A_KIND],
    ['235JJ', HandType.THREE_OF_A_KIND],
    ['J3355', HandType.FULL_HOUSE],
    ['33355', HandType.FULL_HOUSE],
    ['JJ355', HandType.FOUR_OF_A_KIND],
    ['J3555', HandType.FOUR_OF_A_KIND],
    ['J5555', HandType.FIVE_OF_A_KIND],
    ['JJ555', HandType.FIVE_OF_A_KIND],
    ['JJJ55', HandType.FIVE_OF_A_KIND],
    ['JJJJ5', HandType.FIVE_OF_A_KIND],
    ['JJJJJ', HandType.FIVE_OF_A_KIND],
])
def test_part2_hand_classifier(hand, expected_hand_type):
    assert part2_hand_classifier(hand) == expected_hand_type

@mark.parametrize('hand1, hand2, expected_result', [
    ['32T3K', 'T55J5', False],
    ['T55J5', '32T3K', True],
    ['KKKKK', 'QQQQQ', True],
    ['KKKKQ', 'KKKKJ', False],
    ['KKKKK', 'KKKKK', None],
    ['JJJJJ', '22222', False],
])
def test_part2_hand_comparator(hand1, hand2, expected_result):
    assert part2_hand_comparator(hand1, hand2) == expected_result