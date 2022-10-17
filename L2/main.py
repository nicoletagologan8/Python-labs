# This is a sample Python script.
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def fibo(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    result = [0, 1]
    for _i in range(2, n):
        result.append(result[_i - 2] + result[_i - 1])
    return result


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    _max = int(math.sqrt(number))
    for _i in range(3, _max, 2):
        if number % _i == 0:
            return False
    return True


def prime_numbers_in_list(received_list):
    result = []
    for value in received_list:
        if is_prime(value):
            result.append(value)
    return result


def operations_with_lists(list1, list2):
    _intersection = []
    _reunion = []
    _list1_minus_list2 = []
    _list2_minus_list1 = []

    for value1 in list1:
        if value1 in list2 and value1 not in _intersection:
            _intersection.append(value1)
    for value1 in list1:
        _reunion.append(value1)
    for value2 in list2:
        if value2 not in _reunion:
            _reunion.append(value2)
    for value1 in list1:
        if value1 not in _intersection:
            _list1_minus_list2.append(value1)
    for value2 in list2:
        if value2 not in _intersection:
            _list2_minus_list1.append(value2)
    return _reunion, _intersection, _list1_minus_list2, _list2_minus_list1


def song_compose(musical_notes, list_of_moves, start_position):
    result = []
    position = start_position
    result.append(musical_notes[position])
    for _i in list_of_moves:
        position += _i
        if position < 0 or position > len(musical_notes) - 1:
            return "incorrect list of moves"
        result.append(musical_notes[position])
    return result


def replace_matrix_elements(_matrix):
    nr_of_lines = len(_matrix)
    nr_of_columns = len(_matrix[0])
    for _i in range(0, nr_of_lines):
        for j in range(0, nr_of_columns):
            if j < _i:
                _matrix[_i][j] = 0
    return _matrix


def number_of_appearances_in_a_list(input_list, number):
    result = 0
    for value in input_list:
        if value == number:
            result += 1
    return result


def is_palindrome(number):
    temp = number
    rev = 0
    while number > 0:
        rev = rev * 10 + number % 10
        number = number // 10
    if temp == rev:
        return True
    else:
        return False


def palindrome_tuple(list_of_numbers):
    palindrome_numbers = []
    for value in list_of_numbers:
        if is_palindrome(value):
            palindrome_numbers.append(value)
    _max = palindrome_numbers[0]
    for value in palindrome_numbers:
        if value > _max:
            _max = value
    return len(palindrome_numbers), _max


# ex6
def elements_with_x_appearances(*args, x):
    counts = {}
    result = []
    for _list in args:
        for el in _list:
            if counts.get(el):
                counts[el] += 1
            else:
                counts[el] = 1
    print(counts)
    for key in counts.keys():
        if counts[key] == x:
            result.append(key)
    return result


# Press the green button in the gutter to run the script.
def ex8(_list, x=1, flag=True):
    result = []
    for string in _list:
        characters = []
        for character in string:
            if ord(character) % x != flag:
                characters.append(character)
        result.append(characters)
    return result


def ex11(_list):
    _list.sort(key=lambda x: x[1][2])
    return _list


if __name__ == '__main__':
    print_hi('PyCharm')

    # ex1
    print("ex1")
    print("fibo numbers: ")
    print(fibo(10))
    print()

    # ex2
    print("ex2----------------------------------------------------------------------------------")
    print("prime number in list: ")
    print(prime_numbers_in_list([2, 7, 4, 97, 12, 41]))
    print()

    # ex3
    print("ex3----------------------------------------------------------------------------------")
    reunion, intersection, list1_minus_list2, list2_minus_list1 = operations_with_lists([2, 7, 4, 97, 12, 41],
                                                                                        [23, 2, 56, 97, 10])

    print("reunion: ", reunion)
    print("intersection: ", intersection)
    print("list1_minus_list2", list1_minus_list2)
    print("list2_minus_list1", list2_minus_list1)
    print()

    # ex4
    print("ex4----------------------------------------------------------------------------------")
    print(song_compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, -3], 2))
    print()

    # ex5
    print("ex5----------------------------------------------------------------------------------")
    matrix = [
        [2, 5, 6, 2],
        [7, 3, 5, 9],
        [12, 4, 32, 8],
        [65, 2, 0, 2]
    ]
    new_matrix = replace_matrix_elements(matrix)
    print("new matrix: ")
    for i in range(0, len(new_matrix)):
        print(matrix[i])
    print()

    # ex6
    print("ex6----------------------------------------------------------------------------------")
    print(elements_with_x_appearances([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=2))

    # ex7
    print("ex7----------------------------------------------------------------------------------")
    print(palindrome_tuple([12, 121, 45, 88, 34, 11]))

    # ex8
    print("ex8----------------------------------------------------------------------------------")
    print(ex8(x=2, _list=["test", "hello", "lab002"], flag=False))

    # ex9
    print("ex9----------------------------------------------------------------------------------")
    # print(ex9())

    # ex10
    print("ex10----------------------------------------------------------------------------------")
    # print(ex10())

    # ex11
    print("ex11----------------------------------------------------------------------------------")
    print(ex11([('abc', 'bcd'), ('abc', 'zza')]))

    # ex12
    print("ex12----------------------------------------------------------------------------------")
    # print(ex12())
