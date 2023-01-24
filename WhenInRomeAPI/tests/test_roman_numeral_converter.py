from app.roman_numeral_converter import RomanNumeralConverter
import pytest

class TestRomanNumeralConverter:

    def test_convert_to_number_single_digits(self):
        assert RomanNumeralConverter(numeral="I").convert_to_number() == 1
        assert RomanNumeralConverter(numeral="V").convert_to_number() == 5
        assert RomanNumeralConverter(numeral="X").convert_to_number() == 10
        assert RomanNumeralConverter(numeral="L").convert_to_number() == 50

    def test_convert_to_number_single_subtractions(self):
        assert RomanNumeralConverter(numeral="IV").convert_to_number() == 4
        assert RomanNumeralConverter(numeral="IX").convert_to_number() == 9
        assert RomanNumeralConverter(numeral="IV").convert_to_number() == 4
        assert RomanNumeralConverter(numeral="IX").convert_to_number() == 9
        assert RomanNumeralConverter(numeral="IV").convert_to_number() == 4
        assert RomanNumeralConverter(numeral="IX").convert_to_number() == 9

    def test_convert_to_number_invalid_ending(self):
        with pytest.raises(Exception, match="Invalid Numeral: Remaining sequence is larger"):
            RomanNumeralConverter(numeral="CLXIXII").convert_to_number()

    def test_convert_to_number_cannot_be_subtracted(self):
        with pytest.raises(Exception, match="Invalid Numeral: Cannot subtract properly"):
            RomanNumeralConverter(numeral="VIV").convert_to_number()


    def test_convert_to_number_cannot_be_added(self):
        with pytest.raises(Exception, match="Invalid Numeral: I Cannot be added at position 3"):
            RomanNumeralConverter(numeral="IIII").convert_to_number()

        with pytest.raises(Exception, match="Invalid Numeral: V Cannot be added at position 1"):
            RomanNumeralConverter(numeral="VV").convert_to_number()

        with pytest.raises(Exception, match="Invalid Numeral: X Cannot be added at position 4"):
            RomanNumeralConverter(numeral="XIXXX").convert_to_number()

    
    def test_convert_to_number_edge_cases(self):
        assert RomanNumeralConverter(numeral="CDLXXXIX").convert_to_number() == 489

    def test_convert_to_higher_numberes(self):
        assert RomanNumeralConverter(numeral="_I_V").convert_to_number() == 4000


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
        assert RomanNumeralConverter(number=5000).convert_to_roman() == "_V"
        assert RomanNumeralConverter(number=10000).convert_to_roman() == "_X"

    def test_convert_number_to_roman_edge(self):
        assert RomanNumeralConverter(number=9).convert_to_roman() == "IX"
        assert RomanNumeralConverter(number=49).convert_to_roman() == "XLIX"
        assert RomanNumeralConverter(number=132).convert_to_roman() == "CXXXII"
        assert RomanNumeralConverter(number=4000).convert_to_roman() == "_I_V"
        assert RomanNumeralConverter(number=9000).convert_to_roman() == "_I_X"