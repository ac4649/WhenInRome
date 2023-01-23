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
        "M": [ 1000, True, False ]
    }
    
    # By default our numerals are repeatable, but not subtractable
    def __init__(self, numeral : str, bar : bool = False):

        # Returns false if we can't build the valid numeral so we throw an exception
        if not numeral in RomanNumeral.valid_numerals:
            raise Exception("Invalid Numeral")

        self.numeral = numeral
        self.value = RomanNumeral.valid_numerals[self.numeral][0]
        self.repeatable = RomanNumeral.valid_numerals[self.numeral][1]
        self.subtractable = RomanNumeral.valid_numerals[self.numeral][2]