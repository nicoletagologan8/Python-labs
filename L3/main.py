from collections.abc import Iterable


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def ex1(a, b):
    set_a = set(a)
    set_b = set(b)
    result = []
    result.append(set_a.intersection(set_b))
    result.append(set_a.union(set_b))
    result.append(set_a.difference(set_b))
    result.append(set_b.difference(set_a))
    return result


def ex2(string):
    my_dictionary = dict()
    for char in string:
        if char in my_dictionary:
            my_dictionary[char] += 1
        else:
            my_dictionary[char] = 1
    return my_dictionary


def get_all_elements(object):
    if isinstance(object, Iterable) and type(object) != str:
        values = []
        if type(object) == dict:
            for el in object.values():  # atasez toate valorile pe care le poate contine un dictionar
                values += get_all_elements(el)
            for el in object.keys():  # atasex toate cheile pe care le poate contine un dictionar
                values += get_all_elements(el)
        else:
            for el in object:
                values += get_all_elements(el)
        return values
    return [object]


def ex3(dict1, dict2):
    list1 = get_all_elements(dict1)
    list2 = get_all_elements(dict2)
    if len(list1) != len(list2):
        return False
    else:
        for index in range(0, len(list1)):  # verific daca dictionarele au avut cheile si valorile in aceeasi ordine
            if list1[index] != list2[index]:
                return False
        return True


def ex4(tag, content, **params):
    # href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "
    params_join = r''.join(
        p[0] + " = \\\" " + p[1] + " \\ \"" if type(p[1]) == str else p[0] + "= \"" + str(p[1]) + " \"" for p in
        params.items())
    result = "<" + tag + " " + params_join + "> " + content + " </" + tag + ">"
    return result


def ex5(set_of_tuples, dictionary):
    follow_the_rules = 1
    for dict_item in dictionary.items():
        has_key_in_rules = 0
        for tuple in set_of_tuples:
            if tuple[0] == dict_item[0]:
                has_key_in_rules = 1
                if dict_item[1].startswith(tuple[1]) and dict_item[1].endswith(tuple[3]):
                    if tuple[2] in dict_item[1] and (not dict_item[1].startswith(tuple[2])) and (
                            not dict_item[1].endswith(tuple[2])):
                        print("dict item follow the rules")
                    else:
                        follow_the_rules = 0
                else:
                    follow_the_rules = 0
        if has_key_in_rules == 0:
            follow_the_rules = 0
    if follow_the_rules == 1:
        return True
    else:
        return False


def ex6(_list):
    my_dict = dict()
    for value in _list:
        if value in my_dict:
            my_dict[value] += 1
        else:
            my_dict[value] = 1
    a = 0
    b = 0
    for item in my_dict.items():
        if item[1] == 1:
            a += 1
        else:
            b += 1
    return a, b


def ex7(*sets):
    my_dict = {}
    for i in range(0, len(sets) - 1):
        for j in range(i + 1, len(sets)):
            reunion = str(sets[i]) + " | " + str(sets[j])
            intersection = str(sets[i]) + " & " + str(sets[j])
            difference1 = str(sets[i]) + " - " + str(sets[j])
            difference2 = str(sets[j]) + " - " + str(sets[i])
            my_dict[reunion] = sets[i] | sets[j]
            my_dict[intersection] = sets[i] & sets[j]
            my_dict[difference1] = sets[i] - sets[j]
            my_dict[difference2] = sets[i] - sets[j]
    return my_dict


def ex8(dict):
    list_of_objects = []
    visited_keys = []
    current_key = "start"
    # visited_keys.append(current_key)
    # list_of_objects.append(dict[current_key])
    while True:
        if current_key in visited_keys:
            break
        visited_keys.append(current_key)
        if dict[current_key] not in visited_keys:
            list_of_objects.append(dict[current_key])
        current_key = dict[current_key]

    return list_of_objects


def ex9(*args, **kwargs):
    count = 0
    for arg in args:
        ok = 0
        for key, value in kwargs.items():
            if value == arg:
                ok = 1
        if ok == 1:
            count += 1
    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # ex1
    print("ex1------------------------------------------------------")
    print(ex1([1, 4, 3, 8, 5], [1, 20, 3, 2]))
    print()

    # ex2
    print("ex2------------------------------------------------------")
    print(ex2("ananas"))

    # ex3
    print("ex3------------------------------------------------------")

    myDict = {}
    myDict["key1"] = [1, 2]
    lst = ['Ana', 'are', 'mere']
    myDict["key1"].append(lst)
    myDict["key2"] = ["a", "b", "c"]

    myDict2 = {}
    myDict2["key2"] = [1, 2]
    lst2 = ['Ana', 'are', 'mere']
    myDict2["key2"].append(lst)
    myDict2["key1"] = ["a", "b", "c"]

    print(ex3(myDict, myDict2))

    # ex4
    print("ex4------------------------------------------------------")
    print(ex4("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))

    # ex5
    print("ex5------------------------------------------------------")
    print(ex5({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
              {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))

    # ex6
    print("ex6------------------------------------------------------")
    print(ex6(['ana', 3, 9, 12, 3, 'mere', 12, 'ananas']))

    # ex7
    print("ex7------------------------------------------------------")
    print(ex7({1, 2}, {2, 3}, {3, 4}))
    string = ""
    string = string + str({1, 2})
    print(string)

    # ex8
    print("ex8------------------------------------------------------")
    print(ex8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': 'start', 'y': 'start'}))

    # ex9
    print("ex9------------------------------------------------------")
    print(ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
