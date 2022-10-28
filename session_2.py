def reverse_star_printer(number):
    print('*' * number)
    if number != 1:
        reverse_star_printer(number -1)


def power(number, power):
    output = 1
    for i in range(power):
        output = output * number
    return output


def reverse_power(number, power):
    output = number
    if (power > 1):
        output = output * reverse_power(number, power-1)
    return output


def factorail(number):
    result = 1
    for i in range(number+1):
        if i == 0 or i == 1:
            result *= 1
        else:
            result *= i
    return result


def reverse_factorail(number):
    if number == 0:
        return 1
    elif number == 1:
        return number
    else:
        result = 0
        result = number * reverse_factorail(number - 1)
    return result
    


def test_factorail():
    assert factorail(0) == 1
    assert factorail(1) == 1
    assert factorail(2) == 2
    assert factorail(3) == 6


def test_reverse_factorail():
    assert reverse_factorail(0) == 1
    assert reverse_factorail(1) == 1
    assert reverse_factorail(2) == 2
    assert reverse_factorail(3) == 6


def test_power():
    assert power(3,2) == 9
    assert power(3,3) == 27


#print(reverse_power(3, 3))
print(factorail(5))
#print(reverse_factorail(4))

