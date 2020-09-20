from string import ascii_letters
ALPHABET_LENGTH = 26

def is_pangram(sentence):
    return len(set([ch for ch in sentence.lower() if ch in ascii_letters])) == ALPHABET_LENGTH
