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

    def partOfDecimals(self, partOfNum):
        if 1 <= partOfNum <= 3:
            return self.base[1]*partOfNum
        elif partOfNum == 4:
            return self.base[1]+self.base[5]
        elif 5 <= partOfNum <= 8:
            return self.base[5]+((partOfNum - 5)*self.base[1])
        elif partOfNum == 9:
            return self.base[1]+self.base[10]

    def roman(self, num):
        return self.partOfDecimals(num)

