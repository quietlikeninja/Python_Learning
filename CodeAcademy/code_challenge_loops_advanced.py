#https://www.codecademy.com/courses/learn-python-3/articles/advanced-python-code-challenges-loops
def larger_sum(lst1, lst2):
    lst1_sum = 0
    lst2_sum = 0
    for num in lst1:
        lst1_sum += num
    for num in lst2:
        lst2_sum += num
    if lst1_sum >= lst2_sum:
        return lst1
    else:
        return lst2

def larger_sum_no_loop(lst1, lst2):
    if sum(lst1) >= sum(lst2):
        return lst1
    else:
        return lst2

def over_nine_thousand(lst):
    sum = 0
    for num in lst:
        sum += num
        if (sum > 9000):
            break
    return sum

def max_num(nums):
    max = nums[0]
    for num in nums:
        if (num > max):
            max = num
    return max

def same_values(lst1, lst2):
    #matching = []
    #for index in range(len(lst1)):
    #    if (lst1[index] == lst2[index]):
    #        matching.append(index)
    #return matching

    #using list comprehension
    matching = [index for index in range(len(lst1)) if (lst1[index] == lst2[index])]
    return matching

def reversed_list(lst1, lst2):
    for index in range(len(lst1)):
        if lst1[index] != lst2[-1-index]:
            return False
    return True
    
def main():
    #print(larger_sum([1, 9, 2], [2, 3, 7]))
    #print(larger_sum_no_loop([1, 9, 5], [2, 3, 7]))
    #print(over_nine_thousand([8000, 900, 120, 5000]))
    #print(max_num([50, -10, 0, 75, 20]))
    #print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
    print(reversed_list([1, 2, 3], [3, 2, 1]))
    print(reversed_list([1, 5, 3], [3, 2, 1]))

if __name__ == '__main__':
    main()