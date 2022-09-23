#https://www.codecademy.com/courses/learn-python-3/articles/python-code-challenges-loops

def divisible_by_ten(nums):
    count = 0
    for num in nums:
        if (num % 10 == 0):
            count += 1
    return count

def add_greetings(names):
    greetings = []
    for name in names:
        greetings.append("Hello, " + name)
    return greetings

def delete_starting_evens(lst):
    while (len(lst) > 0) and (lst[0] % 2 == 0):
        lst = lst[1:]
    return lst

def odd_indices(lst):
    odd_lst = []
    #my attempt
    #for count, num in enumerate(lst):
    #    if (count % 2 != 0):
    #        odd_lst.append(num)

    #code academy solution
    for index in range(1, len(lst), 2):
        odd_lst.append(lst[index])
    return odd_lst


def main():
    #print(divisible_by_ten([20, 25, 30, 35]))
    #print(add_greetings(["Owen", "Max", "Sophie"]))
    #print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
    #print(delete_starting_evens([4, 8, 10]))
    #print(odd_indices([4, 3, 7, 10, 11, -2]))
    print(exponents([2, 3, 4], [1, 2, 3]))

def exponents(bases, powers):
    new_lst = []
    for base in bases:
        for power in powers:
            new_lst.append(base ** power)
    return new_lst

if __name__ == "__main__":
    main()