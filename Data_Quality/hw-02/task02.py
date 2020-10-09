class Product:
    """Class product."""
    sum = []

    def __init__(self, type_device, name, cost, switch=False):
        self.type_device = type_device
        self.name = name
        self.cost = cost
        self.__class__.sum.append(cost)
        self.switch = switch
        print(f'You have got {self.type_device} {self.name} costing {self.cost}.')

    def switch_on(self):
        """Switch on device."""
        self.switch = True

    def switch_off(self):
        """Switch off device."""
        self.switch = False

    def check_state(self):
        if self.switch:
            print(f'The {self.type_device} {self.name} is switched on.')
        else:
            print(f'The {self.type_device} {self.name} is switched off.')

    @classmethod
    def average_price(cls):
        avg_sum = 0
        for val in cls.sum:
            avg_sum = avg_sum + val
        avg_sum = avg_sum / len(cls.sum)
        print(f'\nThe average price is {round(avg_sum, 2)}')


class TvSet(Product):
    """Class television set."""
    def __init__(self, type_device, name, cost, diagonal):
        super().__init__(type_device, name, cost)
        self.diagonal = diagonal

    def auto_tuning(self):
        """TV set auto-tuned programm."""
        print(f'The TV {self.name} was auto-tuned to cable tv.')

    def __eq__(self, other):
        return self.diagonal == other.diagonal


class Fridge(Product):
    """Class fridge."""
    def __init__(self, type_device, name, cost, count_cam):
        super().__init__(type_device, name, cost)
        self.count_cam = count_cam

    def defrosting(self):
        """Manual defrosting of the refrigerator."""
        print(f'The fridge {self.name} was completely defrost.')

    def __eq__(self, other):
        return self.count_cam == other.count_cam and self.cost == other.cost


# Getting some new devices
tvset1 = TvSet('TV set', 'Sharp', 15000, 14)
tvset2 = TvSet('TV set', 'Sony', 15000, 14)
tvset3 = TvSet('TV set', 'Panasonic', 27000, 21)
tvset4 = TvSet('TV set', 'Sony', 100000, 47)
tvset5 = TvSet('TV set', 'Telefunken', 420000, 98)
fridge1 = Fridge('Fridge', 'Atlant', 28000, 2)
fridge2 = Fridge('Fridge', 'Zanussi', 35000, 3)
fridge3 = Fridge('Fridge', 'Sony', 35000, 3)
fridge4 = Fridge('Fridge', 'Intel', 400000, 7)
fridge5 = Fridge('Fridge', 'AMD', 100000, 5)

# Switching on a TV set to check
print('\nLet\'s switch on a TV set to check and try to tune it.')
tvset1.check_state()
tvset1.switch_on()
tvset1.check_state()
tvset1.auto_tuning()
tvset1.switch_off()
tvset1.check_state()

print('\nLet\'s defrost a fridge.')
fridge4.defrosting()

print('\nLet\'s compare the TV sets.')
if tvset1 == tvset2:
    print(f'The tv set {tvset1.name} equals the tv set {tvset2.name}.')
else:
    print(f'The tv set {tvset1.name} does not equal the tv set {tvset2.name}.')

if tvset1 == tvset5:
    print(f'The tv set {tvset1.name} equals the tv set {tvset5.name}.')
else:
    print(f'The tv set {tvset1.name} does not equal the tv set {tvset5.name}.')

print('\nLet\'s compare the fridges.')
if fridge2 == fridge3:
    print(f'The fridge {fridge2.name} equals the {fridge3.name}.')
else:
    print(f'The fridge {fridge2.name} does not equal the {fridge3.name}.')

if fridge1 == fridge3:
    print(f'The fridge {fridge1.name} equals the {fridge3.name}.')
else:
    print(f'The fridge {fridge1.name} does not equal the {fridge3.name}.')

Product.average_price()