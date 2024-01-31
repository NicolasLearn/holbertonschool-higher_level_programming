#!/usr/bin/python3
def roman_to_int(roman_string):
    dico_rom_digit = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                      'M': 1000}
    sum = 0
    if (type(roman_string) is str) and roman_string:
        index = 0
        while index < len(roman_string):
            char = roman_string[index]
            value = dico_rom_digit[char]
            if char in dico_rom_digit:
                if ((index != len(roman_string) - 1) and
                        (value < dico_rom_digit[roman_string[index + 1]])):
                    index += 1
                    sum += dico_rom_digit[roman_string[index]] - value
                else:
                    sum += dico_rom_digit[roman_string[index]]
            else:
                sum = 0
                break
            index += 1
    return (sum)
