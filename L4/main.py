import os


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


if __name__ == '__main__':
    print_hi('PyCharm')
    print("ex1------------------------------------------------------")
    print(ex1("D:\Facultate\Sem1\Python-labs\L4\Director"))
    print()

    print("ex2------------------------------------------------------")
    ex2("D:\Facultate\Sem1\Python-labs\L4\Director\Director2",
        "D:\Facultate\Sem1\Python-labs\L4\Director\my_file.txt")

    print("ex3------------------------------------------------------")
