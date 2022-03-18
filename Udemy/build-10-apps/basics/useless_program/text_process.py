#!/usr/bin/env python3

def is_question(x):
    if x.startswith("Why") or x.startswith("Where")\
    or x.startswith("Where") or x.startswith("Who")\
    or x.startswith("How") or x.startswith("When"):
        return True
    else:
        return False



sentences = []
 
while True:
    sentence = input("Say something: ").capitalize()
    if sentence == "\end":
        break
    elif is_question(sentence):
        sentence = sentence + "?"
    else:
        sentence = sentence + "."
    sentences.append(sentence)

print(*sentences)