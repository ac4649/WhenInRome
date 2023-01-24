# This class create a roman numeral and keeps properties about it such as repeatability, subtractability ...
# This class also can take a "bar" value of True if the value is multiplied by 1000
class RomanNumeral:

    #TODO: add the ability to use a bar to denote that the digit value is multiplied by 1000
    # The RomanNumeral class contains the valid numerals we can build, and how to actually build them
    valid_numerals = {
        "I": [ 1, True, True ],
        "V": [ 5, False, False ],
        "X": [ 10, True, True ],
        "L": [ 50, False, False ],
        "C": [ 100, True, True ],
        "D": [ 500, False, False ],
        "M": [ 1000, True, False ],
        "_I": [ 1000, True, True ],
        "_V": [ 5000, False, False ],
        "_X": [ 10000, True, True ],

        # We consider the valid subtractions valid roman numerals which are non-repeatable and non-subtractable
        "IV": [ 4, False, False ],
        "IX": [ 9, False, False ],
        "XL": [ 40, False, False ],
        "XC": [ 90, False, False],
        "CD": [ 400, False, False ],
        "CM": [ 900, False, False ],
        "_I_V": [ 4000, False, False ],
        "_I_X": [ 9000, False, False ],
        "_X_L": [ 40000, False, False ],
        "_X_C": [ 90000, False, False ],

    }

    valid_subtractions = ["IV", "IX", "XL", "XC", "CD", "CM","_I_V", "_I_X", "_X_L", "_X_C", "_C_D", "_C_M"]
    
    max_numeral_value = 10000

    @classmethod
    def is_valid_numeral(cls, numeral : str):
        if numeral in RomanNumeral.valid_numerals:
            return True
        return False

    @classmethod
    # Can we subtract numeral 1 from numeral 2
    def is_valid_subtraction(cls, numeral_1 : str, numeral_2 : str):
        combination_value = numeral_1 + numeral_2
        if combination_value in RomanNumeral.valid_subtractions:
            return True
        return False
    
    # By default our numerals are repeatable, but not subtractable
    def __init__(self, numeral : str, bar : bool = False):

        # Returns false if we can't build the valid numeral so we throw an exception
        if not numeral in RomanNumeral.valid_numerals:
            raise Exception("Invalid Numeral")

        self.numeral = numeral
        self.value = RomanNumeral.valid_numerals[self.numeral][0]
        self.repeatable = RomanNumeral.valid_numerals[self.numeral][1]
        self.subtractable = RomanNumeral.valid_numerals[self.numeral][2]

        # We keep track of wether we are done finding this numeral
        self.done_finding = False
        self.found_subtracted_element = False

        # We keep track of the number of times this numeral was found
        self.times_found = 0
        self.sequence_sum = 0

    # A numeral can be subtracted from if:
    # It has not been subtracted from before
    # It hasn't appeared in the sequence yet and is not repeatable
    def canBeSubtractedFrom(self):
        if self.found_subtracted_element:
            return False
        if not self.repeatable and self.times_found > 0:
            return False
        return True

    # A number can be added to the sequence if:
    # It has not been found too many times (based on repeatability)
    # It has not been done being found
    # We have already subtracted from it
    def canBeAdded(self):
        if self.done_finding:
            return False
        if self.found_subtracted_element:
            return False
        if self.times_found > 0:
            if self.repeatable:
                if self.times_found > 2:
                    return False
            else:
                # If we have found the numeral more than 0 times and it isn't repeatable, then we return false
                return False

        return True

    def addToSequence(self):
        # When we add to the sequence, we increment the number of times found and the value of the sequence
        self.times_found += 1
        self.sequence_sum += self.value
        