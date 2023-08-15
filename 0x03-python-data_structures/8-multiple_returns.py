#!/usr/bin/python3
def multiple_returns(sentence):
    sen_length = len(sentence)
    if sen_length == 0:
        output = (0, None)
        return (output)
    else:
        output = (sen_length, sentence[0:1])
        return (sen_length)
