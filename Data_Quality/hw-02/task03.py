class Skier:
    """Class skier."""
    def __init__(self, name, suit, color):
        self.name = name
        self.suit = suit
        self.color = color

    def print_suit(self):
        return f'The skier {self.name} is wearing {self.suit} {self.color} suit.'.capitalize()


class Moving:
    """"Skier movement class"""
    side = {
        'West': 1,
        'East': 1,
        'South': 5
    }

    def __init__(self, start=False):
        self.start = start
        self.val_side = []
        self.distance = 0

    def start_moving(self):
        self.start = True

    def stop_moving(self):
        self.start = False

    def move(self, sec):
        import random as rand
        if not self.start:
            self.start = True
        for key in range(sec):
            self.val_side.append(rand.choice(list(__class__.side.keys())))
        for key in range(sec):
            self.distance += __class__.side[self.val_side[key]]


def main():
    skier1 = Skier('Ivan', 'specialized', 'patterned')
    move1 = Moving()
    seconds = int(input('Enter the count of seconds: '))
    if seconds < 17:
        val = seconds
    else:
        val = 17
    move1.move(val)
    move1.stop_moving()
    print(f'1) For the first {val} seconds, skier {skier1.name} rode: {move1.distance} meters.')
    print(f'2) The skier {skier1.name} was getting down next sides:')
    for slide in move1.val_side:
        print(f'{slide} ', end='')

main()