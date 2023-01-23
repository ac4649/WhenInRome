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
`conda env create -f conda_environment.yml -n WhenInRomeEnv`

activate the env:
`conda activate WhenInRomeEnv`

When the environment is created, please run:
`uvicorn main:app --reload`

This will start the backend in development mode and reload any changed to the files