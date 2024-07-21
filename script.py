import eng_to_ipa as ipa
import sys

words = {}
with open("words.txt") as file:
    for line in file:
        word = line.strip()
        ipa_words = ipa.ipa_list(word)[0]
        words[word] = ipa_words


def display_words(words):
    for key in words:
        print(f"{key}:")
        for word in words[key]:
            print(f" - {word}")
        print("")


# display_words(words)


def main(args):
    if len(args) > 1:
        word = args[1]
        result = ipa.convert(word)
        print(f"{word}: {result}")


if __name__ == "__main__":
    main(sys.argv)
