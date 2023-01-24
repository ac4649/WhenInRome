from app.roman_numeral import RomanNumeral
import pytest

class TestRomanNumeral:

    def test_is_valid_numeral_valid(self):
        assert RomanNumeral.is_valid_numeral("I") == True
        assert RomanNumeral.is_valid_numeral("V") == True
        assert RomanNumeral.is_valid_numeral("X") == True
        assert RomanNumeral.is_valid_numeral("L") == True
        assert RomanNumeral.is_valid_numeral("C") == True
        assert RomanNumeral.is_valid_numeral("D") == True
        assert RomanNumeral.is_valid_numeral("M") == True
        assert RomanNumeral.is_valid_numeral("_I") == True
        assert RomanNumeral.is_valid_numeral("_V") == True
        assert RomanNumeral.is_valid_numeral("_X") == True

    def test_is_valid_numeral_invalid(self):
        assert RomanNumeral.is_valid_numeral("O") == False
        assert RomanNumeral.is_valid_numeral("K") == False

    def test_is_valid_subtraction(self):
        assert RomanNumeral.is_valid_subtraction("I", "V") == True
        assert RomanNumeral.is_valid_subtraction("I", "X") == True
        assert RomanNumeral.is_valid_subtraction("X", "L") == True
        assert RomanNumeral.is_valid_subtraction("X", "C") == True
        assert RomanNumeral.is_valid_subtraction("C", "D") == True
        assert RomanNumeral.is_valid_subtraction("C", "M") == True
        assert RomanNumeral.is_valid_subtraction("_I", "_V") == True
        assert RomanNumeral.is_valid_subtraction("_I", "_X") == True

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

    def test_can_be_subtracted_from(self):
        valid_subtraction = RomanNumeral("X")
        assert valid_subtraction.can_be_subtracted_from() == True
        valid_subtraction.times_found += 2
        assert valid_subtraction.can_be_subtracted_from() == True


        invalid_subtraction = RomanNumeral("V")
        assert invalid_subtraction.can_be_subtracted_from() == True

        # If we found the invalid subtraction once we
        invalid_subtraction.times_found += 1
        assert invalid_subtraction.can_be_subtracted_from() == False