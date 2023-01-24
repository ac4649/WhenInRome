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
    
    def convert_to_number( self ):

        if not self.numeral:
            raise Exception("No Numeral set")


        returned_number = 0
        previous_numerals = {}

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
            if self.numeral[i] == "_":
                try:
                    cur_numeral = RomanNumeral(self.numeral[i:i+2])
                    i += 1
                except Exception as exception:
                    raise exception
            else:
                try:
                    cur_numeral = RomanNumeral(self.numeral[i])
                except Exception as exception:
                    raise exception

            # We check if our current numeral is the same as our previous numeral
            if cur_numeral.numeral in previous_numerals:
                # We have the same numeral, we need to check if we are allowed to repeat it
                if cur_numeral.repeatable:
                    # We need to check that we don't have 3 in a row
                    # We have traversed this numeral more than twice (at least three times) so it is invalid
                    if previous_numerals[cur_numeral.numeral] > 2:
                        raise Exception("Invalid Numeral: 4 or more repeatable numerals")
                else:
                    # WE are not allowed to repeat the numeral
                    raise Exception("Invalid Numeral: non-repeatable numeral is repeated")

            if i + 1 == len(self.numeral):
                # We are on the last numeral, so we break
                returned_number += cur_numeral.value
                break
            else:
                # We need to check if the next number is greater, and if it is we need to subtract if possible
                if self.numeral[i+1] == "_":
                    # If we have a "_" then our indeces for the next number are [i + 1 and i + 2]
                    try:
                        next_numeral = RomanNumeral(self.numeral[i+1:i+3])
                    except Exception as exception:
                        raise exception
                else:
                    try:
                        next_numeral = RomanNumeral(self.numeral[i+1])
                    except Exception as exception:
                        raise exception
                
                if cur_numeral.value < next_numeral.value:
                    if cur_numeral.subtractable:
                        # We are allowed to subtract the current numeral
                        returned_number -= cur_numeral.value
                    else:
                        # We are not allowed to subtract the current numeral, so we throw an error
                        raise Exception("Invalid Numeral: cannot subtract this numeral")
                else:
                    # If the next number isn't greater than our current one, we simply add the value
                    returned_number += cur_numeral.value

            if cur_numeral.numeral in previous_numerals:
                previous_numerals[cur_numeral.numeral] += 1
            else:
                previous_numerals[cur_numeral.numeral] = 1

            i += 1
        # We cache within the object to be able to retrieve later
        self.number = returned_number
        return returned_number

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

