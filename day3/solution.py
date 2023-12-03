from dataclasses import dataclass

@dataclass
class EngineSchematic:
    schematic_data: list[str]

    def is_touching_symbol(self, x: int, y: int) -> bool:
        for test_x in range(x-1, x+2):
            if test_x < 0 or test_x >= len(self.schematic_data):
                continue
            for test_y in range(y-1, y+2):
                if test_x == x and test_y == y:
                    continue
                if test_y < 0 or test_y >= len(self.schematic_data[test_x]):
                    continue
                if self.schematic_data[test_x][test_y] not in '1234567890.':
                    return True
        return False
    
    def get_touching_symbols(self, x: int, y: int) -> bool:
        symbols = []
        for test_x in range(x-1, x+2):
            if test_x < 0 or test_x >= len(self.schematic_data):
                continue
            for test_y in range(y-1, y+2):
                if test_x == x and test_y == y:
                    continue
                if test_y < 0 or test_y >= len(self.schematic_data[test_x]):
                    continue
                if self.schematic_data[test_x][test_y] not in '1234567890.':
                    symbols.append((self.schematic_data[test_x][test_y],test_x,test_y))
        return symbols
    
    def get_part_number_sum(self) -> int:
        current_part_number = ''
        part_number_sum = 0
        is_touching = False
        for x in range(len(self.schematic_data)):
            for y in range(len(self.schematic_data[x])):
                if self.schematic_data[x][y] in '1234567890':
                    current_part_number += self.schematic_data[x][y]
                    if not is_touching and self.is_touching_symbol(x, y):
                        is_touching = True
                else:
                    if current_part_number:
                        if is_touching:
                            part_number_sum += int(current_part_number)
                            is_touching = False
                        current_part_number = ''
        return part_number_sum
    
    def get_gear_ratio_sum(self) -> int:
        current_part_number = ''
        symbols = []
        symbol_map = {}
        for x in range(len(self.schematic_data)):
            for y in range(len(self.schematic_data[x])):
                if self.schematic_data[x][y] in '1234567890':
                    current_part_number += self.schematic_data[x][y]
                    symbols += self.get_touching_symbols(x, y)
                else:
                    if current_part_number:
                        if symbols:
                            for symbol in set(symbols):
                                key = f'{symbol[0]}-{symbol[1]},{symbol[2]}'
                                if key not in symbol_map:
                                    symbol_map[key] = []
                                symbol_map[key].append(int(current_part_number))
                            symbols = []
                        current_part_number = ''
        ratio_sum = 0
        for symbol in symbol_map:
            if symbol.startswith('*') and len(symbol_map[symbol]) == 2:
                ratio_sum += symbol_map[symbol][0] * symbol_map[symbol][1]
        return ratio_sum
    

if __name__ == "__main__":
    with open('day3/input') as f:
        data = [line.strip() for line in f.readlines()]


    es = EngineSchematic(data)
    print(es.get_part_number_sum())
    print(es.get_gear_ratio_sum())