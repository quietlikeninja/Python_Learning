import re


def check_for_name(sentence, name):
    return name.lower() in sentence.lower()

def every_other_letter(word):
    string = ""
    for letter in range(0, len(word), 2):
        string = string + word[letter]
    return string

def every_other_letter_challenge(word):
    string = ""
    for letter in range(0, len(word)):
        if letter % 2 == 0:
            string = string + word[letter]
    return string

def reverse_string(word):
    reverse_word = ""
    if word:
        for letter in range(-1, -len(word)-1, -1):
            reverse_word += word[letter]
    return reverse_word

def make_spoonerism(word1, word2):
    return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

def add_exclamation(word):
    while len(word) < 20:
        word += "!"
    return word

def main():
    print("Should print True: " + str(check_for_name("My name is Jamie", "Jamie")))
    print("Should print True: " + str(check_for_name("My name is jamie", "Jamie")))
    print("Should print False: " + str(check_for_name("My name is Samantha", "Jamie")))
    print("Should print Cdcdm: " + every_other_letter("Codecademy"))
    print("Should print Hlowrd: " + every_other_letter("Hello world!"))
    print("Should print NOTHING: " + every_other_letter(""))
    print("Should print Cdcdm: " + every_other_letter_challenge("Codecademy"))
    print("Should print Hlowrd: " + every_other_letter_challenge("Hello world!"))
    print("Should print NOTHING: " + every_other_letter_challenge(""))
    print("Should print ymedacedoC: " + reverse_string("Codecademy"))
    print("Should print !dlrow olleH: " + reverse_string("Hello world!"))
    print("Should print NOTHING: " + reverse_string(""))
    print("Should print Lodecademy Cearn: " + make_spoonerism("Codecademy", "Learn"))
    print("Should print wello Horld!: " + make_spoonerism("Hello", "world!"))
    print("Should print b a: " + make_spoonerism("a", "b"))
    print("Should print Codecademy!!!!!!!!!!: " + add_exclamation("Codecademy"))
    print("Should print Codecademy is the best place to learn: " + add_exclamation("Codecademy is the best place to learn"))

if __name__ == '__main__':
    main()