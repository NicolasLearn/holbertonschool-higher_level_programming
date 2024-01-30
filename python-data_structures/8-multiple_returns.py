#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    first_char = None
    if lenght > 0:
        first_char = sentence[0]
    return (lenght, first_char)
