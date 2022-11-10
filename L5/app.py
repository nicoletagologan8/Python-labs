import utils


def main():
    while True:
        char = input("Give a number or q: ")
        if char == 'q':
            break
        try:
            x = int(char)
        except Exception as e:
            print("Input must be a number or q")
        else:
            print(utils.process_item(x))


if __name__ == '__main__':
    main()
