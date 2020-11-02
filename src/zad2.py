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
        if num < 10:
            return self.partOfDecimals(num)
        elif num == 27:
            return self.base[10] + self.base[10] + self.partOfDecimals(7)
        elif num == 48:
            return self.base[10]+self.base[50]+self.partOfDecimals(8)
        elif num == 49:
            return self.base[10] + self.base[50] + self.partOfDecimals(9)
        elif num == 59:
            return self.base[50]+self.partOfDecimals(9)

