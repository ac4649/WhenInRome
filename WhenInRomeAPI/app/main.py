from typing import Union
from fastapi import FastAPI

from app.roman_numeral_converter import RomanNumeralConverter

app = FastAPI()

@app.get("/numeral-to-number/")
def convert_roman_to_number_api( numeral : str ):

    converter = RomanNumeralConverter(numeral = numeral)
    try:
        returned_number = converter.convert_to_number()
    except Exception as exception:
        # Will simply return the exception arguments
        return { "error": exception.args[0]}

    return { "number": returned_number }

@app.get("/number-to-numeral")
def convert_roman_to_number_api( number : int | float ):
    print(number)
    try:
        converter = RomanNumeralConverter(number = number)
        returned_numeral = converter.convert_to_roman()
    except Exception as exception:
        return { "error": exception.args[0] }


    return { "numeral": returned_numeral }