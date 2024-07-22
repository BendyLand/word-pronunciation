import eng_to_ipa as ipa


def convert(word):
    return ipa.convert(word)


test = convert("hello")
print(test)

"""
IPA Vowels:

i, y, ɨ, ʉ, w, u
I, Y,         ʊ
e, ø, ɘ, ɵ, ɤ, o
ɛ̝, œ̝,     ʌ̝, ɔ̝
ɛ, œ, ɜ, ɞ, ʌ, ɔ
æ,    ɐ
a, ɶ, ä, ɑ, ɒ
"""
