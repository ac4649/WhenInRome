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
        "_I": [1000, True, True],
        "_V": [5000, False, False],
        "_X": [10000, True, True]
    }
    
    max_numeral_value = 10000

    @classmethod
    def is_valid_numeral(cls, numeral : str):
        if numeral in RomanNumeral.valid_numerals:
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
        