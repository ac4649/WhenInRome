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
        
        if number:
            if isinstance(number, int):
                self.number = number
            else:
                raise Exception("Invalid Number: A given number cannot be decimal")
        else:
            self.number = number

        # We keep track of the numerals we have encountered as we convert
        self.encoutered_numerals = {}

    # We find a numeral starting at position i
    def get_numeral_starting_at_i(self, string : str, i : int, number_chars=1):
        if string[i] == "_":
            new_index = i + number_chars * 2
            # If i start with an underscore, then both chars will have underscore so in any case i will do 2 spaces per character
            numeral_label = string[i:new_index]
        else:
            new_index = i + number_chars
            numeral_label = string[i:new_index]

        if not numeral_label in self.encoutered_numerals:
            try:
                found_numeral = RomanNumeral(numeral_label)
                self.encoutered_numerals[numeral_label] = found_numeral
            except Exception as exception:
                raise exception
        
        # We return the new value of i (which corresponds to the actual index of the letter)
        # I now return the new index - 1 to get the location of the last char
        return self.encoutered_numerals[numeral_label], new_index - 1
    
    def convert_to_number( self ):

        if not self.numeral:
            raise Exception("No Numeral set")

        # We start the summation process by setting the number to 0
        self.number = 0

        # We keep track of the largest value we added
        largest_new_value = None

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
                cur_numeral, new_i = self.get_numeral_starting_at_i(self.numeral, i)
            except Exception as exception:
                raise exception

            if largest_new_value == 0:
                # Can't add anything more, so i raise
                raise Exception("Invalid Numeral: Remaining sequence is larger")
                
            if new_i + 1 == len(self.numeral):
                # We are on the last numeral, so no need to check for anythin after it, just check for whether we can safely add it
                if not cur_numeral.canBeAdded():
                    raise Exception(f'Invalid Numeral: {cur_numeral.numeral} Cannot be added at position {new_i}')
                
                # We check if our new numeral is too large
                if largest_new_value:
                    if largest_new_value < cur_numeral.value:
                        raise Exception("Invalid Numeral: Remaining sequence is larger")

                # And add it to the sequence
                cur_numeral.addToSequence()

                # Every time we end a sequence we update the largest_new_value and the number
                largest_new_value = cur_numeral.maxRestSequenceValue()
                self.number += cur_numeral.value
            else:

                try:
                    # We find the next numeral by sending in new_i + 1 as the position because new_i is the actual position of the character not the "_"\
                    # We save the new position of numeral i to update only if we have a subtraction that is valid
                    next_numeral, next_numeral_i = self.get_numeral_starting_at_i(self.numeral, new_i+1)
                except Exception as exception:
                    raise exception
                
                # We check if we are allowed to subtract the curent numeral from the next one to deal with both as a single numeral
                if RomanNumeral.is_valid_subtraction(cur_numeral.numeral, next_numeral.numeral):
                    # We have a valid subtraction so we need to take it into account
                    # We first check if we can subtract from the next_numeral
                    if not next_numeral.canBeSubtractedFrom():
                        raise Exception("Invalid Numeral: Cannot subtract properly")

                    # If we are allowed to subtract, we generate the new combined numeral
                    try:
                        # I am getting 2 characters here
                        subtraction_numeral, new_i = self.get_numeral_starting_at_i(self.numeral, i, 2)
                    except Exception as exception:
                        raise exception

                    # We must also check if the current subtraction roman numeral can be added (because we cannot have duplicate subtraction symbols)
                    if not subtraction_numeral.canBeAdded():
                        raise Exception(f'Invalid Numeral: {cur_numeral.numeral} Cannot be added at position {new_i}')

                    # We check that we can actually add this subtraction based on the largest value we can add
                    if largest_new_value:
                        if largest_new_value < subtraction_numeral.value:
                            # We are not allowed to subtract the current numeral, so we throw an error
                            raise Exception("Invalid Numeral: Remaining sequence is larger")

                    # We add the subtraction numeral to the sequence
                    subtraction_numeral.addToSequence()

                    next_numeral.found_subtracted_element = True                    
                    
                    # We add our current subtraction numeral's value to the tally
                    self.number += subtraction_numeral.value

                    # And update the maximum sequence value we can add now
                    largest_new_value = subtraction_numeral.maxRestSequenceValue()
                    # We also increment our i to be after the 2nd numeral in the sequence
                    i = next_numeral_i   
                    
                else:
                    # We don't have a valid subtraction so we continue just dealing with the current numeral
                    if not cur_numeral.canBeAdded():
                        raise Exception(f'Invalid Numeral: {cur_numeral.numeral} Cannot be added at position {new_i}')

                    # We check that we can add this new sequence based on the value of the numeral
                    if largest_new_value:
                        if largest_new_value < cur_numeral.value:
                            # We are not allowed to subtract the current numeral, so we throw an error
                            raise Exception("Invalid Numeral: Remaining sequence is larger")

                    # Add it to the sequence to keep tally
                    cur_numeral.addToSequence()

                    # And we find the largest new value we can have
                    largest_new_value = cur_numeral.maxRestSequenceValue()
                    # We also update the tally
                    self.number += cur_numeral.value

                    i = new_i
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

