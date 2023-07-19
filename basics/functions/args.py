def uppercase_words(*args):
    words = [a.upper() for a in args]
    return sorted(words)


print(uppercase_words("example", "one", "word", "blah", "zed"))


def foo(**kwargs):
    return kwargs

print(foo(a=1, b=2, c=4))
