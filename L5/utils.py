def process_item(x):
    x += 1
    ok = 1
    # print(int(x/2))
    for div in range(2, int(x ** (1 / 2)) + 1):
        if x % div == 0:
            ok = 0
    if ok == 1:
        return x
    else:
        return process_item(x)


def main():
    x = int(input("Give a number: "))
    print(process_item(x))


if __name__ == '__main__':
    main()
