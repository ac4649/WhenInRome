from app.roman_numeral import RomanNumeral
import pytest

class TestRomanNumeral:

    def test_known_numerals(self):
        # Here we test the values of the known roman numerals

        assert RomanNumeral("I").numeral == "I"
        assert RomanNumeral("I").value == 1
        assert RomanNumeral("I").repeatable == True
        assert RomanNumeral("I").subtractable == True
        # "I": [ 1, True, True ],
        # "V": [ 5, False, False ],
        # "X": [ 10, True, True ],
        # "L": [ 50, False, False ],
        # "C": [ 100, True, True ],
        # "D": [ 500, False, False ],
        # "M": [ 1000, True, False ]