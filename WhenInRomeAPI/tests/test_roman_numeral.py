from app.roman_numeral import RomanNumeral
import pytest

class TestRomanNumeral:

    def test_known_numerals(self):
        # Here we test the values of the known roman numerals

        assert RomanNumeral("I").numeral == "I"
        assert RomanNumeral("I").value == 1
        assert RomanNumeral("I").repeatable == True
        assert RomanNumeral("I").subtractable == True

        assert RomanNumeral("V").numeral == "V"
        assert RomanNumeral("V").value == 5
        assert RomanNumeral("V").repeatable == False
        assert RomanNumeral("V").subtractable == False
        
        assert RomanNumeral("X").numeral == "X"
        assert RomanNumeral("X").value == 10
        assert RomanNumeral("X").repeatable == True
        assert RomanNumeral("X").subtractable == True

        assert RomanNumeral("L").numeral == "L"
        assert RomanNumeral("L").value == 50
        assert RomanNumeral("L").repeatable == False
        assert RomanNumeral("L").subtractable == False

        assert RomanNumeral("C").numeral == "C"
        assert RomanNumeral("C").value == 100
        assert RomanNumeral("C").repeatable == True
        assert RomanNumeral("C").subtractable == True

        assert RomanNumeral("D").numeral == "D"
        assert RomanNumeral("D").value == 500
        assert RomanNumeral("D").repeatable == False
        assert RomanNumeral("D").subtractable == False

        assert RomanNumeral("M").numeral == "M"
        assert RomanNumeral("M").value == 1000
        assert RomanNumeral("M").repeatable == True
        assert RomanNumeral("M").subtractable == False


    def test_unknown_numeral(self):

        with pytest.raises(Exception, match="Invalid Numeral"):
            RomanNumeral("P")