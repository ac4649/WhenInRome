from typing import Union
from fastapi import FastAPI

from app.roman_numeral_converter import RomanNumeralConverter

app = FastAPI()

@app.get("/numeral-to-number/")
def convert_roman_to_number_api( numeral : str = None ):

    converter = RomanNumeralConverter(numeral = numeral)
    try:
        returned_number = converter.convert_to_number()
    except Exception as exception:
        # Will simply return the exception arguments
        return { "error": exception.args[0]}

    return { "number": returned_number }

@app.get("/number-to-numeral")
def convert_roman_to_number_api( number : int | float = None):
    try:
        converter = RomanNumeralConverter(number = number)
        returned_numeral = converter.convert_to_roman()
    except Exception as exception:
        return { "error": exception.args[0] }


    return { "numeral": returned_numeral }


@app.get("/roman_addition")
def roman_addition( numeral1 : str = None, numeral2 : str = None):
    try:
        converter1 = RomanNumeralConverter(numeral = numeral1)
        converter2 = RomanNumeralConverter(numeral = numeral2)
        converted_number1 = converter1.convert_to_number()
        converted_number2 = converter2.convert_to_number()
        summation = converted_number1 + converted_number2
        summation_converter = RomanNumeralConverter(number=summation)
        returned_numeral = summation_converter.convert_to_roman()
    except Exception as exception:
        return { "error": exception.args[0] }


    return { "numeral": returned_numeral }