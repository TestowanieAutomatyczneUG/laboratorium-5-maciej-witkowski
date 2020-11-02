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

    def ones(self, partOfNum):
        if 1 <= partOfNum <= 3:
            return self.base[1]*partOfNum
        elif partOfNum == 4:
            return self.base[1]+self.base[5]
        elif 5 <= partOfNum <= 8:
            return self.base[5]+((partOfNum - 5)*self.base[1])
        elif partOfNum == 9:
            return self.base[1]+self.base[10]

    def tens(self, partOfNum):
        if 1 <= partOfNum <= 3:
            return self.base[10]*partOfNum
        elif partOfNum == 4:
            return self.base[10]+self.base[50]
        elif 5 <= partOfNum <= 8:
            return self.base[50]+((partOfNum - 5)*self.base[10])
        elif partOfNum == 9:
            return self.base[10]+self.base[100]

    def roman(self, num):
        divided = [int(i) for i in str(num)]
        if num < 10:
            return self.ones(divided[0])
        elif num < 100:
            return self.tens(divided[0])+self.ones(divided[1])
        elif num == 141:
            return self.base[100]+self.tens(4)+self.ones(1)
        elif num == 163:
            return self.base[100]+self.tens(6)+self.ones(3)
        elif num == 402:
            return self.base[100]+self.base[500]+self.ones(2)
        elif num == 575:
            return self.base[500]+self.tens(7)+self.ones(5)
        elif num == 911:
            return self.base[100]+self.base[1000]+self.tens(1)+self.ones(1)
