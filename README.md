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

### Note about numbers with a bar on top

For numbers with a bar on top, the unicode symbols do not exist or they would have been used
So they are encoded by adding an underscore in front of the letter:

_I

_V

_X

...

The front end will parse the "_" and display the text-decoration: overline instead

## Installation and Running

### Running the backend
The backend uses FastAPI, it is recommended to use a conda environment if running locally to ensure that the requirements are met. Miniforge is recommended (https://github.com/conda-forge/miniforge)

To run the backend, start by running `cd WhenInRomeAPI` to go into the backend api directory

The conda environment dependencies required are defined in "conda_environment.yml"

To create the conda environment with the requirements you can run:

`conda env create -f conda_environment.yml -n WhenInRomeEnv`

activate the env:

`conda activate WhenInRomeEnv`

When the environment is created, please run:
`uvicorn app.main:app --reload`

To run the unit tests run:

`pytest`

This will start the backend in development mode and reload any changed to the files

### Running the Front End

The front end is a NextJS application which was built using yarn (https://yarnpkg.com).
In order to run the front end, use Yarn

Create a ".env.local" file (sample.env.local file for reference) containing the Backend url to which the Front end should connect

then do `yarn install` from the "WhenInRomeFE" directory

then to run the application `yarn dev` to run in development mode
