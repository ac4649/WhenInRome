# WhenInRome
Roman Numeral conversion using Python and NextJS

The goal of this project is to create an app using NextJS and FastAPI which enables a user to convert a Roman Numeral into it's Arabic Numeral counterpart. The api will also be able to convert an Arabic Numeral into its Roman Numeral counterpart.



## Infrastructure

The Front End is a NextJS application which utilizes NextJS API Routes to communicate with the backend api. The code for this is in the WhenInRomeFE directory.

The Back End is a FastAPI application which will have routes for the various tasks performed. The code for this is in the WhenInRomeAPI directory.

Routes and there descriptions are described below:
### /numeral-to-number
Parameters: numeral (string)
Returns: {
    number: ###
}

### /number-to-numeral
Parameters: number
Returns: {
    numeral: ""
}


## Installation and Running

### Running the backend
The backend uses FastAPI, it is recommended to use a conda environment if running locally to ensure that the requirements are met.

To run the backend, start by running `cd WhenInRomeAPI` to go into the 

The conda environments required are defined in "conda_environment.yml"

To create the conda environment with the requirements you can run:
`conda env create -f conda_environment.yml`

When the environment is created, please run:
`uvicorn main:app --reload`

This will start the backend in development mode and reload any changed to the files

## Methodology

### Roman Numeral to Number:

We have a dictionary of values for the that each Roman Numeral can take:
{
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9
    "X": 10,
    "XL": 40,
    "L": 50,
    "LC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
    ...   
}

We start by having the returned value be 0.
We first check if the 2 first characters of the string are a key to the roman numeral dictionary.
If they are we remove them from the string and add the corresponding value to the returned value
If we don't find the 2 first characters as a key, then we check for the first character only, and add it's value
If we don't find anything we return an error message saying that we have an invalid Roman Numeral input

Example:
Roman Numeral: DLXIV

Value = 0
Step 1: Check for DL => no key, check "D" -> D is 500 so we add it => value = 500, remaining_string = "LXIV"
Step 2: Check for LX => no key, check "L" -> L is 50 => value = 550, remaining_string = "XIV"
Step 3: Check for XC => no key, check "X" -> X is 10 => value = 560, remaining_string = "IV"
Step 4: Check for IV => IV = 4, so we add it => value = 564, remaining_string = ""
We are done



### Number to Roman Numeral
