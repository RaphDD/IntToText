class IntToTextConvertor:

    def __init__(self):
        # maximum value
        self.MAX_VAL = 999999999999
        # numbers from 0-20
        self.negative_word = "moins "
        # self list of low numbers in increasing order
        self.low_numbers = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept",
                            "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze",
                            "quinze", "seize", "dix-sept", "dix-huit", "dix-neux"]
        # tens in decreasing oreder, used to decompose the number
        self.tens = [("quatre-vingt-dix", 90), ("quatre-vingt", 80), ("soixante-dix", 70), ("soixante", 60), ("cinquante", 50),
                      ("quarante", 40), ("trente", 30), ("vingt", 20)]
        # bases in decreasing order, used to decompose the number
        self.bases = [("milliard", 1000000000), ("million", 1000000), ("mille", 1000)]

    def convert_sub_thousand(self, number):
        """
        Function used to perform conversions for numbers between 0-999 inclusive.
        :param number: the number to transfrom
        :return: the textual representation of the number
        """
        # if the number is  between 0-19 just return the value straight from the list
        if number < 20:
            return self.low_numbers[number]
        output = ""
        # determine if there are hundreds there
        result = divmod(number, 100)
        if result[0] > 0:
            # if there is more than one hundred add the specific number
            if result[0] > 1:
                output += self.low_numbers[result[0]]+" "
            output += "cent "
        # set the number to the remainder
        number = result[1]
        # if the new number is  between 0-19 just add the value
        if 0 < number < 20:
            output += self.low_numbers[number]+" "
            return output
        # determine tens in number
        for ten in self.tens:
            result = divmod(number, ten[1])
            # if the quotient is non-negative write out the tens unit
            if result[0] > 0:
                output += ten[0]
                # interrupt the loop if we find teh tens
                break

        # add the final low number to the end using special case and non special cases
        if ten[1] in [70,90]:
            # deal with 77-79 and 97-99
            if result[1] > 6:
                output += f"-{self.low_numbers[result[1]]}"
            # deal with 72-76 and 92-96
            elif result[1] > 1:
                # remove the last "dix" with the correct equivalent
                output = output[:-3]+self.low_numbers[result[1]+10]
            else:
                # deal with 71 and 91 case with no hyphens
                output = output[:-4]+" et "+self.low_numbers[result[1]+10]
        # deal with quatre-vingt-un
        elif ten[1] == 80:
            output += f"-{self.low_numbers[result[1]]}"
        else:
            # deal with "et un case"
            if result[1] == 1:
                output += f" et un"
            elif result[1] > 1:
                output += f"-{self.low_numbers[result[1]]}"

        return output

    def convert(self, number):
        """
        Function to convert a number to its textual representation. Calls the convert_sub_thousand function to work.
        :param number: the number to be converted
        :return: the textual representation of the number
        """
        # check number is inferior to the maxvalue possible of 999999999999.
        if number > self.MAX_VAL:
            print(f"Number {number} exceeds maximum conversion size of {self.MAX_VAL}. Returning an empty string...")
            return ""
        # start with an empty string
        output = ""
        # verify if the number is negative. If so start with the negative word first and
        # use the absolute value for further processing
        if number < 0:
            number = abs(number)
            output = self.negative_word

        # if the number is  between 0-19 just return the value straight from the list
        if number < 20:
            output += self.low_numbers[number]
            return output

        # otherwise start decomposing the number using bases
        for base in self.bases:
            result = divmod(number, base[1])
            # if quotient is non-negative we have something to write out
            if result[0] > 0:
                # add an s to the base if required (mille never takes an s)
                if base[0] in ["million", "milliard"] and result[0] != 1:
                    clean_base = base[0]+"s"
                else:
                    clean_base = base[0]
                # if the base is 1000 and there is a single one do not add "un"
                if base[0] == "mille" and result[0] == 1:
                    output += "mille "

                # general case: pass the quotient to the sub thousand converter and write it with the base
                else:
                    output += f"{self.convert_sub_thousand(result[0])} {clean_base} "

            # continue the process with the remainder
            number = result[1]
        if number != 0:
            output += f"{self.convert_sub_thousand(number)}"
        return self.clean_number(output)

    def convert_multiple(self, numbers: [int]):
        """
        Convert multiple numbers from a list
        :param numbers: the list of numbers
        :return: th elist of string representations
        """
        output = []
        for number in numbers:
            output.append(self.convert(number))
        return output

    def clean_number(self, number:str):
        """
        Clean up the final string representation of the number
        :param number: the string to clean
        :return: the cleaned string
        """
        number = number.strip()
        # plural if ends with 80
        array = number.split()
        if array[-1] == "quatre-vingt":
            number += "s"
        # decompose number into array to verify plural for cent
        elif len(array) > 1 and array[-1] == "cent" and array[-2] in self.low_numbers:
            number += "s"
        return number
