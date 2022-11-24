import os
import re


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# def ex1(text):
#     list = []
#     word = ""
#     for char in text:
#         if char.isdigit() or char.isalpha():
#             word = word + char
#         else:
#             if len(word) > 0:
#                 list.append(word)
#                 word = ""
#     if len(word) > 0:
#         list.append(word)
#     return list

def ex1(text):
    regex = '[a-zA-Z0-9]+'
    arr = re.findall(regex, text)
    return arr


def ex2(regex_string, text_string, number):
    arr = re.findall(regex_string, text_string)
    y = filter(lambda x: len(x) == number, arr)
    return list(y)


def ex3(list_string, list_regex):
    list = []
    for string in list_string:
        for el_reg in list_regex:
            if re.search(el_reg, string):
                list.append(string)
                break

    return list


def ex4(path, attrs):
    result = []
    f = open(path, "r")
    content = f.read()
    elements = re.findall("<\w+.*?>", content)
    for el in elements:
        if (all([re.search(item[0] + "\s*=\s*\"" + item[1] + "\"", el, flags=re.I) for item in attrs.items()])):
            result += [el]
    return result


def ex5(path, attrs):
    result = []
    f = open(path, "r")
    content = f.read()
    elements = re.findall('<\w+.*?>', content)
    for el in elements:
        if (any([re.search(item[0] + "\s*=\s*\"" + item[1] + "\"", el, flags=re.I) for item in attrs.items()])):
            result += [el]
    return result


def replacing(string):
    s = string.group(0).lower()
    if s[0] in "aeiou" and s[len(s) - 1] in "aeiou":
        new_s = ""
        for index, ch in enumerate(string.group(0)):
            if index % 2 == 0:
                new_s = new_s + ch
            else:
                new_s = new_s + "*"
        return new_s
    else:
        return string.group(0)


def ex6(text):
    return re.sub("\w+", replacing, text)


def ex7(cnp_string):
    return re.match(
        "[1256]\d\d(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[1-2])(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$",
        cnp_string) != None


def ex8(directory, reg_expr):
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_name = os.path.join(root, file)
            print(file_name)
            match = re.search(reg_expr, file)
            if match:
                try:
                    f = open(file_name, "r")
                    content = f.read()
                    if re.search(reg_expr, content):
                        result += ["<<" + file]
                    else:
                        result += [file]
                except:
                    pass
            else:
                try:
                    f = open(file_name, "r")
                    content = f.read()
                    if re.search(reg_expr, content):
                        result += [file]
                except:
                    pass
        return result


if __name__ == '__main__':
    print_hi('PyCharm')
    print("ex1---------------------------------------------")
    print(ex1("Ana are mere 78"))
    print()

    print("ex2---------------------------------------------")
    print(ex2('[a-zA-Z0-9]+', "Ana are mere a78", 3))

    print("ex3---------------------------------------------")
    print(ex3(["fna", "are", "mere", "23$", "24"], ['^f']))


    print("ex6---------------------------------------------")
    print(ex6("Ana are mere"))

    print("ex7---------------------------------------------")
    print(ex7("6221109017608"))

    print("ex8---------------------------------------------")
    print(ex8("D:\Facultate\Sem1\Python-labs\L6", "^f"))
