def star_printer():
    number = int(input("Please Enter The Number: "))
    for i in range(number):
        stars = "*" * (i+1)
        spaces = " " * (number - 2)
        print(spaces + stars)


def squar_printer():
    number = int(input("Please Enter The Number: "))
    print("*" * number)
    for i in range(number-2):
        print("*"+(" " * (number-2))+"*")
    print("*" * number)

def polygon_printer():
    number = int(input("Please Enter The Number: "))
    for i in range(number-1):
        print(((number-i-1)*' ') + ("*" * i) + "*" + ("*" * i) + ((number-i-1)*' '))

    print("*" * (number-1) + "*" + "*" * (number-1))
        
    for i in range(number-1):
        print(((i+1)*' ') + ("*" * (number-i-2)) + "*" + ("*" * (number-i-2)) + ((i+1)*' '))

polygon_printer()
