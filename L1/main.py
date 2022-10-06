import math

def gcd_multiple_numbers():
    number = int(input('Enter number of numbers: '));
    arr = []
    while number:
        nr = int(input())
        arr.append(nr)
        number = number - 1
    current_div = arr[0]
    for index in range(1, len(arr)):
        current_div = math.gcd(current_div, arr[index])
    print("The greatest common divisor: ")
    print(current_div)

def nr_of_vowels():
    string = input("Enter a string: ")
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    nr_vowels = 0
    for index in range(0, len(string)):
        if string[index] in vowels:
            nr_vowels = nr_vowels + 1
    print("Number of vowels: ")
    print(nr_vowels)


def number_of_occurrences():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    len1 = len(string1)
    len2 = len(string2)
    nr_occurrences = 0

    for index in range(len1 - len2 + 1):
        j = 0
        while j < len2:
            if string1[j + index] != string2[j]:
                break
            j += 1

        if j == len2:
            nr_occurrences += 1
            j = 0
    print("number_of_occurrences: ")
    print(nr_occurrences)
    # print(string1.count(string2));


def toLowerCaseWithUnderscore():
    string = input("Enter the initial string: ")
    for index in range(0, len(string)):
        if string[index].isupper() and index == 0:
            string = string[:index] + string[index].lower() + string[index + 1:]
        elif string[index].isupper() and index != 0:
            string = string[:index] + '_' + string[index].lower() + string[index + 1:]
            index += index
    print("lower case with underscore result: ")
    print(string)


def spiralOrderMatrix(arr, i, j, m):
    # If i or j lies outside the matrix

    strResult = ""
    while i < m and j < m:
        # Print First Row
        for p in range(i, m):
            # strResult += "{}".format(arr[i][p])
            strResult += arr[i][p]

        # Print Last Column
        for p in range(i + 1, m):
            strResult += arr[p][m - 1]

        # Print Last Row
        for p in range(m - 2, j - 1, -1):
            strResult += arr[m - 1][p]

        # Print First Column
        for p in range(m - 2, i, -1):
            strResult += arr[p][j]

        i += 1
        j += 1
        m -= 1
    print("result string: ")
    print(strResult)


def isPalindrome():
    num = int(input("Enter a value:"))
    temp = num
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10
    if temp == rev:
        print("This value is a palindrome number!")
    else:
        print("This value is not a palindrome number!")


def extractNumberFromAText():
    text = input("Enter a text: ")
    digitFound = False
    number = 0

    for index in range(0, len(text)):
        if (text[index].isdigit()):
            digitFound = True
            number = number * 10 + int(text[index])
        else:
            if digitFound == True:
                break
    if digitFound:
        print(number)
    else:
        print("No number found")
        

def numberOfBits():
    number = int(input("Enter a number: "))
    # print("Bits with value 1: ", bin(number).count("1"))

    binary = 0
    ctr = 0
    temp=number
    while temp :
        binary = ((temp%2)*(10**ctr)) + binary
        temp = int(temp/2)
        ctr += 1
    
    print("Bits with value 1: ", bin(number).count("1"))

def mostCommonLetter():
    string = input("Enter a string: ")
    arr = [0] * 123
    for index in range (0, len(string)):
        arr[ord(string[index])]+=1
    max=arr[0]
    commonLetter=' '
    for index in range (0, len(arr)):
        if arr[index] > max and chr(index) != ' ':
            max=arr[index]
            commonLetter=chr(index)
    print(f"Most common letter: {commonLetter} ({max} times)")

def wordsInAText():
    text = input("Enter a text: ")
    spaces=0

    for index in range (0, len(text)):
        if text[index] == ' ':
            spaces+=1
    
    print("Number of words: ", spaces+1)


if __name__ == '__main__':
    # ex1
    # gcd_multiple_numbers()

    # ex2
    # nr_of_vowels()

    # ex3
    #number_of_occurrences()

    # ex4
    # toLowerCaseWithUnderscore()

    # ex5
    L = 4
    arr = [['f', 'i', 'r', 's'],
           ['n', '_', 'l', 't'],
           ['o', 'b', 'a', '_'],
           ['h', 't', 'y', 'p']]
    spiralOrderMatrix(arr, 0, 0, L)

    # ex6
    # isPalindrome()

    # ex7
    #extractNumberFromAText()

    # ex8
    #numberOfBits()

    # ex9
    # mostCommonLetter()

    # ex10
    # wordsInAText()


