import sys
import eng_to_ipa as ipa


def main(args):
    if len(args) > 1:
        word = args[1]
        result = ipa.convert(word)
        print(f"{word}: {result}")
    else:
        print("Please provide a word.")


if __name__ == "__main__":
    main(sys.argv)
