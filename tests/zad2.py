import unittest
from src.zad2 import RomanNumerals


class RomanNumeralsTest(unittest.TestCase):
    def test_1_is_a_single_i(self):
        self.assertEqual(self.romanNumerals.roman(1), "I")

    @unittest.skip("not implemented")
    def test_2_is_two_i_s(self):
        self.assertEqual(self.romanNumerals.roman(2), "II")

    @unittest.skip("not implemented")
    def test_3_is_three_i_s(self):
        self.assertEqual(self.romanNumerals.roman(3), "III")

    @unittest.skip("not implemented")
    def test_4_being_5_1_is_iv(self):
        self.assertEqual(self.romanNumerals.roman(4), "IV")

    @unittest.skip("not implemented")
    def test_5_is_a_single_v(self):
        self.assertEqual(self.romanNumerals.roman(5), "V")

    @unittest.skip("not implemented")
    def test_6_being_5_1_is_vi(self):
        self.assertEqual(self.romanNumerals.roman(6), "VI")

    @unittest.skip("not implemented")
    def test_9_being_10_1_is_ix(self):
        self.assertEqual(self.romanNumerals.roman(9), "IX")

    @unittest.skip("not implemented")
    def test_20_is_two_x_s(self):
        self.assertEqual(self.romanNumerals.roman(27), "XXVII")

    @unittest.skip("not implemented")
    def test_48_is_not_50_2_but_rather_40_8(self):
        self.assertEqual(self.romanNumerals.roman(48), "XLVIII")

    @unittest.skip("not implemented")
    def test_49_is_not_40_5_4_but_rather_50_10_10_1(self):
        self.assertEqual(self.romanNumerals.roman(49), "XLIX")

    @unittest.skip("not implemented")
    def test_50_is_a_single_l(self):
        self.assertEqual(self.romanNumerals.roman(59), "LIX")

    @unittest.skip("not implemented")
    def test_90_being_100_10_is_xc(self):
        self.assertEqual(self.romanNumerals.roman(93), "XCIII")

    @unittest.skip("not implemented")
    def test_100_is_a_single_c(self):
        self.assertEqual(self.romanNumerals.roman(141), "CXLI")

    @unittest.skip("not implemented")
    def test_60_being_50_10_is_lx(self):
        self.assertEqual(self.romanNumerals.roman(163), "CLXIII")

    @unittest.skip("not implemented")
    def test_400_being_500_100_is_cd(self):
        self.assertEqual(self.romanNumerals.roman(402), "CDII")

    @unittest.skip("not implemented")
    def test_500_is_a_single_d(self):
        self.assertEqual(self.romanNumerals.roman(575), "DLXXV")

    @unittest.skip("not implemented")
    def test_900_being_1000_100_is_cm(self):
        self.assertEqual(self.romanNumerals.roman(911), "CMXI")

    @unittest.skip("not implemented")
    def test_1000_is_a_single_m(self):
        self.assertEqual(self.romanNumerals.roman(1024), "MXXIV")

    @unittest.skip("not implemented")
    def test_3000_is_three_m_s(self):
        self.assertEqual(self.romanNumerals.roman(3000), "MMM")

    # Utility functions
    def setUp(self):
        self.romanNumerals = RomanNumerals()