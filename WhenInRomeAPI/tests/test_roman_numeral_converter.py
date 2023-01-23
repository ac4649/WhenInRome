from app.roman_numeral_converter import RomanNumeralConverter
import pytest

class TestRomanNumeralConverter:

    def test_convert_to_number_single_digits(self):
        assert RomanNumeralConverter(numeral="I").convert_to_number() == 1
        assert RomanNumeralConverter(numeral="V").convert_to_number() == 5
        assert RomanNumeralConverter(numeral="X").convert_to_number() == 10
        assert RomanNumeralConverter(numeral="L").convert_to_number() == 50