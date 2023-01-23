# We create a RomanNumeralConverter class which will enable the conversion functionality
from roman_numeral import RomanNumeral

class RomanNumeralConverter:
    def __init__(self, numeral : str = None, number : int = None):
        self.numeral = numeral
        self.number = number
    
    def convert_to_number( self ):

        if not self.numeral:
            raise Exception("No Numeral set")


        returned_number = 0
        cur_numeral_count = 0
        previous_numeral = ""
        error = False
        
        # Let's start by going throught the numeral string and counting all the roman digits we find
        # We then do checks for the rules:
        # 1. We check that repeatable numerals are only present 3 times
        # 2. We check that non-repeatable numerals are not present more than once
        # 3. We subtract subtractable numerals from the sum if we are allowed to
        for i in range(len(self.numeral)):
            # We create the roman numeral for the current character
            try:
                cur_numeral = RomanNumeral(self.numeral[i])
            except:
                return "Invalid Numeral"
            
            # We check if our current numeral is the same as our previous numeral
            if previous_numeral == cur_numeral.numeral:
                # We have the same numeral, we need to check if we are allowed to repeat it
                if cur_numeral.repeatable:
                    # We need to check that we don't have 3 in a row
                    if cur_numeral_count > 3:
                        return "Invalid Numeral"
                else:
                    # WE are not allowed to repeat the numeral
                    return "Invalid Numeral"
            else:
                cur_numeral_count = 1

            if i + 1 == len(self.numeral):
                # We are on the last numeral
                returned_number += cur_numeral.value
            else:
                # We need to check if the next number is greater, and if it is we need to subtract if possible
                try:
                    next_numeral = RomanNumeral(self.numeral[i+1])
                except:
                    return "Invalid Numeral"
                
                if cur_numeral.value < next_numeral.value:
                    if cur_numeral.subtractable:
                        # We are allowed to subtract the current numeral
                        returned_number -= cur_numeral.value
                    else:
                        # We are not allowe to subtract the current numeral, so we throw an error
                        return "Invalid Numeral"
                else:
                    # If the next number isn't greater than our current one, we simply add the value
                    returned_number += cur_numeral.value


            previous_numeral = cur_numeral.numeral
            cur_numeral_count += 1

        self.number = returned_number
        return returned_number

    def convert_to_roman(self):
        print("converting the number to roman")
        if not self.number:
            raise Exception("No Number set")

        # The basic conversion of a number to roman numerals is to find the largest number we can subtract by and replace with the appropriate roman numeral and do this until we reach 0
        