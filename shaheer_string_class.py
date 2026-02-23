class StringPlay:
    def __init__(self, str):
        self.str = str

    def upper_case(self):
        upper_case = self.str.upper()
        return upper_case

    def lower_case(self):
        lower_case = self.str.lower()
        return lower_case

    def captalize_case(self):
        capital = self.str.capitalize()
        return capital

    def case_fold_case(self):
        case_fold_case = self.str.casefold()
        return case_fold_case

    def split_case(self):
        split_case = self.str.split()
        return split_case

    def is_lower_case(self):
        is_lower_case = self.str.islower()
        return is_lower_case

    def is_upper_case(self):
        is_upper_case = self.str.isupper()
        return is_upper_case

    def is_digit(self):
        is_digit = self.str.isdigit()
        return is_digit

    def is_space(self):
        is_space = self.str.isspace()
        return is_space

    def is_numeric(self):
        is_numeric = str.isnumeric()
        return is_numeric

    def is_alpha_case(self):
        is_alpha_case = str.isalpha()
        return is_alpha_case

    def swap_case(self):
        swap_case = str.swapcase()
        return swap_case

    def is_alnum(self):
        is_alnum = str.isalnum()
        return is_alnum

str = 'This is the month of Ramazan. I keep fast.'
string_play = StringPlay(str)
