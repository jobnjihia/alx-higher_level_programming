#!/usr/bin/python3
def multiple_returns(sentence):
    sen_length = len(sentence)

    if sen_length == 0:
        return (0, None)
    else:
        return (sen_length, sentence[0])
