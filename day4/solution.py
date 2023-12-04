from dataclasses import dataclass, field
import re
from typing import Self

@dataclass
class ScratchCard:
    card_number: int = 0
    winning_numbers: list[int] = field(default_factory=list)
    play_numbers: list[int] = field(default_factory=list)

    @staticmethod
    def from_data_line(data_line: str) -> 'ScratchCard':
        parts = re.split(':|\|', data_line)
        result = ScratchCard()
        result.card_number = int(parts[0].strip().split(" ")[-1])
        result.winning_numbers = [int(i) for i in parts[1].strip().split(" ") if i]
        result.play_numbers = [int(i) for i in parts[2].split(" ") if i]
        return result
    
    @property
    def part1_points(self) -> int:
        points = 0
        for number in self.play_numbers:
            if number in self.winning_numbers:
                points += points or 1
        return points
    
    @property
    def win_count(self) -> int:
        count = 0
        for number in self.play_numbers:
            if number in self.winning_numbers:
                count += 1
        return count

if __name__ == "__main__":
    with open("day4/input") as f:
        data = f.readlines()

    total_part1_points = 0
    cards = []
    for line in data:
        card = ScratchCard.from_data_line(line)
        cards.append({"card":card,"count":1})
        total_part1_points += card.part1_points

    print(total_part1_points)

    for index, card in enumerate(cards):
        for wins in range(card['card'].win_count):
            cards[index+wins+1]["count"] += cards[index]["count"]

    total_cards = 0
    for entry in cards:
        total_cards += entry["count"]

    print(total_cards)
