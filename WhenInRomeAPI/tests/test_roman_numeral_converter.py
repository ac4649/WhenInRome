from app.roman_numeral_converter import RomanNumeralConverter
import pytest

class TestRomanNumeralConverter:

    def test_convert_to_number_single_digits(self):
        assert RomanNumeralConverter(numeral="I").convert_to_number() == 1
        assert RomanNumeralConverter(numeral="V").convert_to_number() == 5
        assert RomanNumeralConverter(numeral="X").convert_to_number() == 10
        assert RomanNumeralConverter(numeral="L").convert_to_number() == 50


    def test_convert_to_number_duplicate_entries(self):
        with pytest.raises(Exception, match="Invalid Numeral: non-repeatable numeral is repeated"):
            RomanNumeralConverter(numeral="VIV").convert_to_number()

        with pytest.raises(Exception, match="Invalid Numeral: 4 or more repeatable numerals"):
            RomanNumeralConverter(numeral="IIII").convert_to_number()
        
        with pytest.raises(Exception, match="Invalid Numeral: 4 or more repeatable numerals"):
            RomanNumeralConverter(numeral="XIXXX").convert_to_number()
    

    def test_convert_number_to_roman_error(self):
        with pytest.raises(Exception, match="No Number set"):
            RomanNumeralConverter().convert_to_roman()

        with pytest.raises(Exception, match="Roman Numerals must be > 0"):
            RomanNumeralConverter(number=-1).convert_to_roman()

    def test_convert_number_to_roman_simple(self):
        assert RomanNumeralConverter(number=1).convert_to_roman() == "I"
        assert RomanNumeralConverter(number=5).convert_to_roman() == "V"
        assert RomanNumeralConverter(number=10).convert_to_roman() == "X"
        assert RomanNumeralConverter(number=50).convert_to_roman() == "L"

    def test_convert_number_to_roman_edge(self):
        assert RomanNumeralConverter(number=9).convert_to_roman() == "IX"
        assert RomanNumeralConverter(number=49).convert_to_roman() == "XLIX"
        assert RomanNumeralConverter(number=132).convert_to_roman() == "CXXXII"