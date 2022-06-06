#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    firstLetter = sentence[0]
    lts = [length, firstLetter]
    if len(lts) == 0:
        return
    else:
        return tuple(lts)
