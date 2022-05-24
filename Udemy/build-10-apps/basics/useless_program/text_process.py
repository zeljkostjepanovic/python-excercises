#!/usr/bin/env python3

def sentence_maker(x):
    interrogatives = ('Why', 'Where', 'Who', 'How', 'When', 'What')
    x = x.capitalize()
    if x.startswith(interrogatives):
        return "{}?".format(x)
    else:
        return "{}.".format(x)


results = []

while True:
    user_input = input("Say something: ")
    if "\end" in user_input:
        print("==============")
        print("Your input below:")
        print("==============")
        print(user_input, sep=" ")
        break
    else:
        results.append(sentence_maker(user_input))
