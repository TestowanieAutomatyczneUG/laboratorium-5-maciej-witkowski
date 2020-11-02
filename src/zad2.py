class RomanNumerals:
    def __init__(self):
        self.base = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }

    def roman(self, num):
        if num == 1:
            return self.base[1]
        elif num == 2:
            return self.base[1]+self.base[1]
        elif num == 3:
            return self.base[1]+self.base[1]+self.base[1]
        elif num == 4:
            return self.base[1]+self.base[5]
        elif num == 5:
            return self.base[5]
        elif num == 6:
            return self.base[5]+self.base[1]
        elif num == 9:
            return self.base[1]+self.base[10]

