#!/bin/python


from math import ceil


def get_number():
    while True:
        enter = input("Enter a number you would like to check for prime: ")
        try:
            enter = int(enter)
            return enter
        except ValueError:
            print("This is not a valid input for a natural number")


def round_number(rounded):
    rounded = rounded ** (1 / 2)
    rounded = ceil(rounded)
    return rounded


def check_for_prime(num, root_num):
    for i in range(2, root_num):
        if num % i == 0:
            return False
        elif i == root_num - 1:
            return True
        else:
            continue


if __name__ == '__main__':
    number = get_number()
    root = round_number(number)

    if check_for_prime(number, root):
        print("This number is prime! ")
    else:
        print("This number is not prime")
