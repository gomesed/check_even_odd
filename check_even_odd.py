def is_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

if __name__ == '__main__':
    number = int(input("Enter an integer number: "))
    is_even(number)
