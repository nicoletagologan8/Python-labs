import os
import sys


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def ex1(director):
    unique_extensions = set()
    for file in os.listdir(director):
        if os.path.isfile(os.path.join(director, file)):
            var = os.path.splitext(file)
            unique_extensions.add(var[1][1:])
    return sorted(list(unique_extensions))


def ex2(director, file):
    try:
        file_to_write = open(file, "w")
        for f in os.listdir(director):
            join_path = os.path.join(director, f)
            if os.path.isfile(join_path) and f[0] == "A":
                file_to_write.write(os.path.abspath(join_path))
                file_to_write.write(os.linesep)
    except Exception as e:
        print(str(e))


def ex3(my_path):
    if os.path.isfile(my_path):
        file = open(my_path, 'rb')
        size = os.path.getsize(my_path)
        try:
            assert (size >= 20), "File should contain more than 19 characters"
        except Exception as e:
            print(e)
        file.seek(size - 20)
        buffer = file.read()
        return buffer
    elif os.path.isdir(my_path):
        dictionary = dict()
        for (root, directories, files) in os.walk(my_path):
            for file in files:
                extension = os.path.splitext(file)[1]
                # print(extension)
                extension = extension[1:]
                if extension in dictionary:
                    dictionary[extension] += 1
                else:
                    dictionary[extension] = 1
        _list = [(k, v) for k, v in dictionary.items()]
        return sorted(_list, key=lambda el: el[1], reverse=True)
    else:
        raise Exception("Exception")


def ex4():
    try:
        assert (len(sys.argv) > 1), "One parameter is needed"
        assert (os.path.isdir(sys.argv[1])), "Parameter is not a director"
        list = []
        for el in os.listdir(sys.argv[1]):
            if os.path.isfile(os.path.join(sys.argv[1], el)):
                extension = os.path.splitext(el)[1]
                extension = extension[1:]
                if extension != "":
                    if extension not in list:
                        list.append(extension)
        return sorted(list)
    except Exception as e:
        print(str(e))
        return []


def ex5(target, to_search):
    _list = []
    if os.path.isfile(target):
        f = open(target, "r")
        file_content = f.read()
        if to_search in file_content:
            return [target]
    elif os.path.isdir(target):
        for (root, directories, files) in os.walk(target):
            for file in files:
                full_path = os.path.join(root, file)
                f = open(full_path, "r")
                file_content = f.read()
                if to_search in file_content:
                    _list.append(full_path)
        return _list
    else:
        raise ValueError("Target needs to be a file or a directory")


def display_error(error):
    print("error is: ", error)


def ex6(target, to_search, callback):
    try:
        return ex5(target, to_search)
    except Exception as e:
        callback(e)
        return []


def ex7(file_path):
    dictionary = dict()
    try:
        assert (os.path.isfile(file_path)), "File path expected"
        dictionary["full_path"] = os.path.abspath(file_path)
        dictionary["file_size"] = os.path.getsize(file_path)
        dictionary["file_extension"] = os.path.splitext(file_path)[1][1:]
        dictionary["can_read"] = os.access(file_path, os.R_OK)
        dictionary["can_write"] = os.access(file_path, os.W_OK)
        return dictionary
    except Exception as e:
        print(str(e))
        return {}


def ex8(dir_path):
    _list = []
    try:
        for el in os.listdir(dir_path):
            full_path = os.path.join(dir_path, el)
            if os.path.isfile(full_path):
                _list.append(os.path.abspath(full_path))
        return _list
    except Exception as e:
        print(str(e))
        return []


if __name__ == '__main__':
    print_hi('PyCharm')
    print("ex1------------------------------------------------------")
    print(ex1("D:\Facultate\Sem1\Python-labs\L4\Director"))
    print()

    print("ex2------------------------------------------------------")
    ex2("D:\Facultate\Sem1\Python-labs\L4\Director\Director2",
        "D:\Facultate\Sem1\Python-labs\L4\Director\my_file.txt")
    print()

    print("ex3------------------------------------------------------")
    print(ex3("D:\Facultate\Sem1\Python-labs\L4\Director"))
    print()

    print("ex4------------------------------------------------------")
    # print(ex4())

    print("ex5------------------------------------------------------")
    print(ex5("D:\Facultate\Sem1\Python-labs\L4\Director", "mere"))
    print()

    print("ex6------------------------------------------------------")
    print(ex6("D:\Facultate\Sem1\Python-labs\L4\Director", "mere", display_error))

    print("ex7------------------------------------------------------")
    print(ex7("D:\Facultate\Sem1\Python-labs\L4\Director\search_file.txt"))
    print()

    print("ex8------------------------------------------------------")
    print(ex8("D:\Facultate\Sem1\Python-labs\L4\Director"))
