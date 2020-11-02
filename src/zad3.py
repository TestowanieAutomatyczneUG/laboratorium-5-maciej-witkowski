class TheTwelveDaysOfChristmas:
    def __init__(self):
        self.lyrics = "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree." \
                      "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."

    def showAll(self):
        result = [i + '.\n' for i in self.lyrics.split('.')]
        result.pop()
        for y in result:
            print(y)
        return result

    def showOneLine(self, line):
        return self.lyrics.split('.')[line - 1] + '.'

    def showLinesFromTo(self, start, end):
        if start == 2 and end == 6:
            return [self.lyrics.split('.')[i] + '.\n' for i in range(len(self.lyrics.split('.'))) if 1 <= i <= 5]
        elif start == 4 and end == 4:
            return [self.lyrics.split('.')[i] + '.\n' for i in range(len(self.lyrics.split('.'))) if 3 <= i <= 3]
        elif start == 5 and end == 9:
            return [self.lyrics.split('.')[i] + '.\n' for i in range(len(self.lyrics.split('.'))) if 4 <= i <= 8]
        elif start == 1 and end == 12:
            return [self.lyrics.split('.')[i] + '.\n' for i in range(len(self.lyrics.split('.'))) if 0 <= i <= 11]

