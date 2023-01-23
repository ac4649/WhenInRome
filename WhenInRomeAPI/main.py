from typing import Union
from fastapi import FastAPI

from roman_numeral_converter import RomanNumeralConverter

app = FastAPI()

@app.get("/numeral-to-number/")
def convert_roman_to_number_api( numeral : str ):

    converter = RomanNumeralConverter(numeral)
    returned_number = converter.convert_to_number()

    return { "number": returned_number }

@app.get("/number-to-numeral")
def convert_roman_to_number_api():
    returned_numeral = ""
    return { "numeral": returned_numeral }