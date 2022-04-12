#!/usr/bin/env python3

def sentence_maker(x):
    interrogatives = ('Why', 'Where', 'Who', 'How', 'When', 'What')
    x = x.capitalize()
    if x.startswith(interrogatives):
        return "{}?".format(x)
    else:
        return "{}.".format(x)


while True:
    sentence = input("Say something: ")
    if sentence != "\end":
        print(sentence_maker(sentence))
    else:
        break
