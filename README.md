# IntToText
A small script that allows the user to translate a numerical representation of an integer into its  textual form (in French). 
The form taken by the output corresponds to the traditional metropolitan france spelling, pre-1990 spelling reform. 

## Input
The input is provided to the program via a command line interface argument. This argument is a string representation of an array. See the example usage below if need be.

## Output
The output is printed out to the CLI, as a list containing the textual equivalents in the same order as was provided via the input.

## Mode 
The default execution mode of this program relies on a local implementation of a convertor. this problem has however
already been solved so in real world conditions, we would probably use the num2words implementation. Setting the mode parameter
to `num2words` will do just that. 

## Example Usage

``python IntToText.py -i "[1,2,3,5,7,8,10,100,156,235,1598,1578963215]"``