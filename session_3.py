def ds_not_mf():
    new_list = []

    for j in range(2000, 3200):
        if j % 7 == 0 and j % 5 != 0:
            new_list.append(j)

    print(new_list)

def ds_not_mf_while():
    start = 2000
    end = 3200

    count = start

    while count <= end:
        if count % 7 == 0 and count % 5 != 0:
            print(count)
        count += 1

def fibonacci(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def seq_fibonacci(nterms):
    # check if the number of terms is valid
    if nterms <= 0:
       print("Plese enter a positive integer")
    else:
       print("Fibonacci sequence:")
       for i in range(nterms):
           print(fibonacci(i))


def find_course_average():
    summ = 0
    student_a = {
	"first" : "Amir",
	"last": "Douzandeh",
	"courses": 25,
	"isStudent" : False,
	}
    student_b = {
	"first" : "Ali",
	"last": "Zen",
	"courses": 32,
	"isStudent" : True,
	}
    b = [student_a, student_b, student_a, student_b]

    for student in b:
        summ += student["courses"]

    print(summ / len(b))


def titlecase(string):
    index = 0
    sepreted_string = string.split(" ")
    for i in sepreted_string:
        sepreted_string[index] = i[0].upper() + i[1:]
        index += 1

    print(' '.join(sepreted_string))
    

def write_in_file():
    with open('sample.txt', mode='w') as file:
        file.write('Hello World!')

def read_from_file():
    with open('sample.txt', mode='r') as file:
        for record in file:
            print(record)

def append_in_file():
    with open('sample.txt', mode='a+') as file:
        file.write('\n Hello World! #4\n')
    

def write_stars_append():
    number = int(input("Please Enter The Number: "))
    for i in range(number):
        with open('stars.txt', mode='a+') as file:
            file.write(("*" * (i + 1) + '\n'))
    

def write_stars_write():
    number = int(input("Please Enter The Number: "))
    with open('stars.txt', mode='w') as file:
        for i in range(number):
            file.write(("*" * (i + 1) + '\n'))


def expand_stars():
    total_lines = 0
    number = int(input("Please Enter The Number: "))
    with open('stars.txt', mode='r+') as file:
        for count, line in enumerate(file):
            pass

        total_lines = count + 1

    with open('stars.txt', mode='a+') as file:
        for i in range(total_lines, number):
            file.write(("*" * (i + 1) + '\n'))
        
    

expand_stars()



