from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/numeral-to-number")
def convert_roman_to_number():
    returned_number = 0
    return { "number": returned_number }

@app.get("/number-to-numeral")
def convert_roman_to_number():
    returned_numeral = ""
    return { "numeral": returned_numeral }