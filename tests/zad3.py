import unittest
from src.zad3 import TheTwelveDaysOfChristmas


class TheTwelveDaysOfChristmasTest(unittest.TestCase):
    @unittest.skip("not implemented")
    def testShowAll(self):
        self.assertEqual(self.song.showAll(), [
            'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\n',
            'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n'
        ])

    @unittest.skip("not implemented")
    def testFirstLine(self):
        self.assertEqual(self.song.showOneLine(1), 'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.')

    @unittest.skip("not implemented")
    def testSecondLine(self):
        self.assertEqual(self.song.showOneLine(2), 'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.')

    @unittest.skip("not implemented")
    def testThirdLine(self):
        self.assertEqual(self.song.showOneLine(3), 'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    @unittest.skip("not implemented")
    def testFourthLine(self):
        self.assertEqual(self.song.showOneLine(4), 'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    @unittest.skip("not implemented")
    def testFifthLine(self):
        self.assertEqual(self.song.showOneLine(5), 'On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    @unittest.skip("not implemented")
    def testSixthLine(self):
        self.assertEqual(self.song.showOneLine(6), 'On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    @unittest.skip("not implemented")
    def testSeventhLine(self):
        self.assertEqual(self.song.showOneLine(7), 'On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    @unittest.skip("not implemented")
    def testEighthLine(self):
        self.assertEqual(self.song.showOneLine(8), 'On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    @unittest.skip("not implemented")
    def testNinthLine(self):
        self.assertEqual(self.song.showOneLine(9), 'On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    @unittest.skip("not implemented")
    def testTenthLine(self):
        self.assertEqual(self.song.showOneLine(10), 'On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    @unittest.skip("not implemented")
    def testEleventhLine(self):
        self.assertEqual(self.song.showOneLine(11), 'On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    @unittest.skip("not implemented")
    def testTwelfthLine(self):
        self.assertEqual(self.song.showOneLine(12), 'On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    @unittest.skip("not implemented")
    def testShowLinesFromTo_2_6(self):
        self.assertEqual(self.song.showLinesFromTo(2, 6), [
            'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n'
        ])

    @unittest.skip("not implemented")
    def testShowLinesFromTo_4_4(self):
        self.assertEqual(self.song.showLinesFromTo(4, 4), [
            'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n'
        ])

    @unittest.skip("not implemented")
    def testShowLinesFromTo_5_9(self):
        self.assertEqual(self.song.showLinesFromTo(5, 9), [
            'On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n'
        ])

    @unittest.skip("not implemented")
    def testShowLinesFromTo_1_12(self):
        self.assertEqual(self.song.showLinesFromTo(1, 12), [
            'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\n',
            'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n'
        ])

    @unittest.skip("not implemented")
    def testShowLinesFromTo_7_8(self):
        self.assertEqual(self.song.showLinesFromTo(7, 8), [
            'On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n'
        ])

    @unittest.skip("not implemented")
    def testLineNotInt(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.showOneLine("8")

    @unittest.skip("not implemented")
    def testLineBiggerThan12(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.showOneLine(15)

    @unittest.skip("not implemented")
    def testLineSmallerThan1(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.showOneLine(0)

    @unittest.skip("not implemented")
    def testFirstLineNotInt(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.showLinesFromTo("", 9)

    @unittest.skip("not implemented")
    def testSecondLineNotInt(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.showLinesFromTo(10, "11")

    @unittest.skip("not implemented")
    def testDisallowFirstLineBiggerThanSecond(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.showLinesFromTo(8, 4)

    @unittest.skip("not implemented")
    def testDisallowFirstLineSmallerThan1(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.showLinesFromTo(-8, 2)

    @unittest.skip("not implemented")
    def testDisallowSecondLineBiggerThan12(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.showLinesFromTo(5, 21)

    @unittest.skip("not implemented")
    def testDisallowBothLinesOffTheScale(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.showLinesFromTo(14, 18)

    # Utility functions
    def setUp(self):
        self.song = TheTwelveDaysOfChristmas()
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")
