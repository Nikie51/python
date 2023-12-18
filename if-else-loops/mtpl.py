#!/usr/bin/env python3

def multiple_returns(sentence):
    if not sentence:
        return None

    return (len(sentence), sentence[0])

