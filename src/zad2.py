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
        else:
            return ""

    def tens(self, partOfNum):
        if 1 <= partOfNum <= 3:
            return self.base[10]*partOfNum
        elif partOfNum == 4:
            return self.base[10]+self.base[50]
        elif 5 <= partOfNum <= 8:
            return self.base[50]+((partOfNum - 5)*self.base[10])
        elif partOfNum == 9:
            return self.base[10]+self.base[100]
        else:
            return ""

    def hundreds(self, partOfNum):
        if 1 <= partOfNum <= 3:
            return self.base[100] * partOfNum
        elif partOfNum == 4:
            return self.base[100] + self.base[500]
        elif 5 <= partOfNum <= 8:
            return self.base[500] + ((partOfNum - 5) * self.base[100])
        elif partOfNum == 9:
            return self.base[100] + self.base[1000]
        else:
            return ""

    def roman(self, num):
        divided = [int(i) for i in str(num)]
        if num < 10:
            return self.ones(divided[0])
        elif num < 100:
            return self.tens(divided[0])+self.ones(divided[1])
        elif num < 1000:
            return self.hundreds(divided[0])+self.tens(divided[1])+self.ones(divided[2])
        elif num == 1024:
            return self.base[1000]+self.hundreds(0)+self.tens(2)+self.ones(4)

