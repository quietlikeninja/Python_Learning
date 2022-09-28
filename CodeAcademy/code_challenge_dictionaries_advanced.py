from mimetypes import init


#https://www.codecademy.com/courses/learn-python-3/articles/advanced-python-code-challenges-dictionaries

def word_length_dictionary(words):
    word_length = {}
    for word in words:
        word_length[word] = len(word)
    return word_length

def frequency_dictionary(words):
    frequency = {}
    for word in words:
        if word not in frequency:
            frequency[word] = 0
        frequency[word] += 1
    return frequency

def unique_values(my_dictionary):
    uniques = []
    for value in my_dictionary.values():
        if value not in uniques:
            uniques.append(value)
    return len(uniques)

def count_first_letter(names):
    letters = {}
    for last_name, first_names in names.items():
        if last_name[0] not in letters:
            letters[last_name[0]] = 0
        letters[last_name[0]] += len(first_names)
    return letters

def main():
    print("Should print {\"apple\":5, \"dog\": 3, \"cat\":3}: " + str(word_length_dictionary(["apple", "dog", "cat"])))
    print("Should print {\"a\": 1, \"\": 0}: " + str(word_length_dictionary(["a", ""])))
    print("Should print {\"apple\":2, \"cat\":1, 1:1}: " + str(frequency_dictionary(["apple", "apple", "cat", 1])))
    print("Should print {0:5}: " + str(frequency_dictionary([0,0,0,0,0])))
    print("Should print 2: " + str(unique_values({0:3, 1:1, 4:1, 5:3})))
    print("Should print 1: " + str(unique_values({0:3, 1:3, 4:3, 5:3})))
    print("Should print {\"S\": 4, \"L\": 3}: " + str(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]})))
    print("Should print {\"S\": 7}: " + str(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]})))

if __name__ == '__main__':
    main()