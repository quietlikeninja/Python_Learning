def sum_values(my_dictionary):
    sum = 0
    for value in my_dictionary.values():
        sum += value
    return sum

def sum_even_keys(my_dictionary):
    sum = 0
    for index in my_dictionary.keys():
        if index % 2 == 0:
            sum += my_dictionary[index]
    return sum

def add_ten(my_dictionary):
    for key in my_dictionary.keys():
        my_dictionary[key] += 10
    return my_dictionary

def values_that_are_keys(my_dictionary):
    new_list = []
    for value in my_dictionary.values():
        if value in my_dictionary.keys():
            new_list.append(value)
    return new_list

def max_key(my_dictionary):
    largest_key = float("-inf")
    largest_value = float("-inf")
    for key, value in my_dictionary.items():
        if value > largest_value:
            largest_key = key
            largest_value = value
    return largest_key

def main():
    print("Should print 10: " + str(sum_values({"milk":5, "eggs":2, "flour": 3})))
    print("Should print 6: " + str(sum_values({10:1, 100:2, 1000:3})))
    print("Should print 2: " + str(sum_even_keys({1:5, 2:2, 3:3})))
    print("Should print 6: " + str(sum_even_keys({10:1, 100:2, 1000:3})))
    print("Should print {1:15, 2:12, 3:13}: " + str(add_ten({1:5, 2:2, 3:3})))
    print("Should print {10:11, 100:12, 1000:13}: " + str(add_ten({10:1, 100:2, 1000:3})))
    print("Should print [1, 4]: " + str(values_that_are_keys({1:100, 2:1, 3:4, 4:10})))
    print("should print [\"a\"]: " + str(values_that_are_keys({"a":"apple", "b":"a", "c":100})))
    print("Should print 1: " + str(max_key({1:100, 2:1, 3:4, 4:10})))
    print("Should print c: " + max_key({"a":100, "b":10, "c":1000}))

if __name__ == '__main__':
    main()