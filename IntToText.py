from argparse import ArgumentParser
from IntToTextConvertor import IntToTextConvertor
from num2words import num2words
import json


def parse_args():
    """
    Build the argument parser and return the arguments parsed from the command line.
    :return:
    """
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", type=str,
                        help="The input sequence of numbers to translate into text.",
                        required=True)
    parser.add_argument("-m", "--mode", type=str, default="custom",
                        help="Operating mode. Defaults to 'custom' which is our local implementation."
                             " Can be set to num2words instead to use their implementation.",
                        choices=["custom", "num2words"])
    return parser.parse_args()


if __name__ == "__main__":

    # parse the CLI arguments
    args = parse_args()
    # use the json library to read the string into an array of integers
    try:
        number_list = json.loads(args.input)
    except Exception as e:
        print(f"Error reading the input: {e}! Check the format. See readme for example usage.")
        exit(1)

    # use num2words instead of the local implementation
    if args.mode == "num2words":
        output_list = []
        for number in number_list:
            output_list.append(num2words(number, lang=args.format))

        print(output_list)
        exit(0)
    # use the local implementation
    else:
        # build the convertor
        convertor = IntToTextConvertor()
        # pass the data to the convertor
        text_numbers = convertor.convert_multiple(number_list)
        # print the resulting list
        print(text_numbers)

