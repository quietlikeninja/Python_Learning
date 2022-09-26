def unique_english_letters(word):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    count = 0
    for letter in letters:
        if letter in word:
            count += 1
    return count

def unique_english_letters_2(word):
    count = 0
    used_letters = []
    for letter in word:
        if letter not in used_letters:
            count += 1
            used_letters.append(letter)
    return count

def count_char_x(word, x):
    count = 0
    for letter in word:
        if letter == x:
            count += 1
    return count

def count_multi_char_x(word, x):
    return len(word.split(x)) -1

def substring_between_letters(word, start, end):
    if word.find(start) != -1 and word.find(end, word.find(start)) != -1:
        return word[word.find(start)+1:word.find(end)]
    else:
        return word

def x_length_words(sentence, x):
    words = sentence.split()
    for word in words:
        if len(word) < x:
            return False
    return True

def main():
    print("Should print 4: " + str(unique_english_letters("mississippi")))
    print("Should print 4: " + str(unique_english_letters("Apple")))
    print("Should print 4: " + str(count_char_x("mississippi", "s")))
    print("Should print 1: " + str(count_char_x("mississippi", "m")))
    print("Should print 2: " + str(count_multi_char_x("mississippi", "iss")))
    print("Should print 1: " + str(count_multi_char_x("apple", "pp")))
    print("Should print pl: " + str(substring_between_letters("apple", "p", "e")))
    print("Should print apple: " + str(substring_between_letters("apple", "p", "c")))
    print("Should print False: " + str(x_length_words("i like apples", 2)))
    print("Should print True: " + str(x_length_words("he likes apples", 2)))

if __name__ == '__main__':
    main()