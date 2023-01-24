# We create a RomanNumeralConverter class which will enable the conversion functionality
from app.roman_numeral import RomanNumeral
import re

class RomanNumeralConverter:
    def __init__(self, numeral : str = None, number : int = None):
        # We want to pre-process the numeral by removing any whitespace chars from it
        if numeral:
            self.numeral = re.sub(r"\s+", "", numeral)
        else:
            self.numeral = numeral
            
        self.number = number

        # We keep track of the numerals we have encountered as we convert
        self.encoutered_numerals = {}

    # We find a numeral starting at position i
    def get_numeral_starting_at_i(self, string : str, i : int):
        if string[i] == "_":
            numeral_label = string[i:i+2]
            i += 1
        else:
            numeral_label = string[i]

        if not numeral_label in self.encoutered_numerals:
            try:
                found_numeral = RomanNumeral(numeral_label)
                self.encoutered_numerals[numeral_label] = found_numeral
            except Exception as exception:
                raise exception
            
        # We return the new value of i (which corresponds to the actual index of the letter)
        return self.encoutered_numerals[numeral_label], i
    
    def convert_to_number( self ):

        if not self.numeral:
            raise Exception("No Numeral set")

        # We start the summation process by setting the number to 0
        self.number = 0
        # We keep track of the smallest value we added    
        # This is because we can never add more than the previously smallest added value.
        smallest_value_added = RomanNumeral.max_numeral_value

        # Let's start by going throught the numeral string and counting all the roman digits we find
        # We then do checks for the rules:
        # 1. We check that repeatable numerals are only present 3 times
        # 2. We check that non-repeatable numerals are not present more than once
        # 3. We subtract subtractable numerals from the sum if we are allowed to
        i = 0

        while i < len(self.numeral):
            # We create the roman numeral for the current character
            # We know that the numerals can have their value multiplied by 1000 if they have a bar on top,
            # We represent this bar on top with a "_" symbol before the character
            try:
                cur_numeral, i = self.get_numeral_starting_at_i(self.numeral, i)
            except Exception as exception:
                raise exception

            if i + 1 == len(self.numeral):
                # We are on the last numeral, so no need to check for anythin after it, just check for whether we can safely add it
                if not cur_numeral.canBeAdded():
                    raise Exception("Invalid Numeral: Cannot be added properly")
                added_value = cur_numeral.value
            else:

                try:
                    # We find the next numeral by sending in i + 1 as the position
                    next_numeral, new_i = self.get_numeral_starting_at_i(self.numeral, i+1)
                except Exception as exception:
                    raise exception

                if cur_numeral.value < next_numeral.value:

                    if not next_numeral.canBeSubtractedFrom():
                        raise Exception("Invalid Numeral: Cannot subtract properly")

                    if cur_numeral.subtractable:
                        # We are allowed to subtract the current numeral
                        added_value = next_numeral.value - cur_numeral.value
                        i = new_i
                    else:
                        # We are not allowed to subtract the current numeral, so we throw an error
                        raise Exception("Invalid Numeral: cannot subtract this numeral")

                    # Because our next numeral is larger than our current one, we are done looking for our next numeral
                    next_numeral.found_subtracted_element = True

                else:
                    # We check if we can add the current numeral to the string

                    if not cur_numeral.canBeAdded():
                        raise Exception("Invalid Numeral: Cannot be added properly")
                    
                    # If the next number isn't greater than our current one, we simply add the value of the current one
                    # We do it here because if the next number has a greater value, neither really counts towards the total in the sequence
                    added_value = cur_numeral.value
                    
                    # In any case, we up the number of times found
                    cur_numeral.times_found += 1

            if added_value > smallest_value_added:
                raise Exception("Invalid Numeral: larger value to the right of a smaller value")
            else:
                # If we still have a valid roman numeral string, we update the smallest value added
                smallest_value_added = added_value

            self.number += added_value
            i += 1
        return self.number

    def convert_to_roman(self):

        if not self.number:
            raise Exception("No Number set")

        if self.number < 0:
            raise Exception("Roman Numerals must be > 0")

        remainder = self.number
        # The basic conversion of a number to roman numerals is to find the largest number we can subtract by and replace with the appropriate roman numeral and do this until we reach 0
        # Base case if we don't have a valid number we will return an exception
        returned_numeral = ""

        conversion_table = {
            10000: "_X",
            9000: "_I_X",
            5000: "_V",
            4000: "_I_V",
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        for key in conversion_table.keys():
            # Our key represents the current value
            while remainder / key >= 1:
                # While we can subtract the current value, we do so
                returned_numeral += conversion_table[key]
                remainder -= key            


        # We cache within the object to be able to retrieve later
        self.numeral = returned_numeral
        return returned_numeral

