def ex2(*args, **kwargs):
    sum = 0
    for key, value in kwargs.items():
        sum += value
    return sum


def ex3(string):
    def function(string):
        _list = []
        for char in string:
            if char in "aeiouAEIOU":
                _list.append(char)
        return _list

    anonymous_function_ex3 = lambda string: [ch for ch in string if ch in 'aeiouAEIOU']
    filter_function = lambda string: list(filter(lambda char: char in 'aeiouAEIOU', string))

    result1 = function(string)
    result2 = anonymous_function_ex3(string)
    result3 = filter_function(string)
    return result1, result2, result3


def ex4(*args, **kwargs):
    dictionaries_list = []
    for arg in args:
        if type(arg) is dict:
            if len(list(arg.keys())) >= 2:
                for key in arg.keys():
                    if len(str(key)) >= 3:
                        dictionaries_list.append(arg)
                        break
    for value in kwargs.values():
        if type(value) is dict:
            if len(list(value.keys())) >= 2:
                for key in value.keys():
                    if len(str(key)) >= 3:
                        dictionaries_list.append(value)
                        break

    return dictionaries_list


def ex5(_list):
    new_list = []
    for item in _list:
        if type(item) in [int, float, complex]:
            new_list.append(item)
    return new_list


def ex6(_list):
    even_numbers = []
    odd_numbers = []
    for el in _list:
        if el % 2 == 0:
            even_numbers.append(el)
        else:
            odd_numbers.append(el)
    tuples = []
    for i in range(0, len(even_numbers)):
        tuples.append((even_numbers[i], odd_numbers[i]))
    return tuples


anonymous_function = lambda *args, **kwargs: sum([value for key, value in kwargs.items()])


def ex9(pairs):
    _list_of_dictionaries = []
    for pair in pairs:
        dictionary = {}
        dictionary["sum"] = pair[0] + pair[1]
        dictionary["prod"] = pair[0] * pair[1]
        dictionary["pow"] = pair[0] ** pair[1]
        _list_of_dictionaries.append(dictionary)
    return _list_of_dictionaries

if __name__ == '__main__':
    print(ex2(1, 2, c=3, d=4))
    print(anonymous_function(1, 2, c=3, d=4))

    print(ex3("Programming in Python is fun"))

    print(ex4(
        {1: 2, 3: 4, 5: 6},

        {'a': 5, 'b': 7, 'c': 'e'},

        {2: 3},

        [1, 2, 3],

        {'abc': 4, 'def': 5},

        3764,

        dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

        test={1: 1, 'test': True}
    )
    )

    print(ex5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))

    print(ex6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

    print(ex9(pairs=[(5, 2), (19, 1), (30, 6), (2, 2)]))
