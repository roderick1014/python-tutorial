# Python Tutorial - Iterators



def iterFunction():
    my_list = [1, 2, 3, 4, 5]
    my_iter = iter(my_list)

    print(next(my_iter))   # prints 1
    print(next(my_iter))   # prints 2
    print(next(my_iter))   # prints 3
    print(next(my_iter))   # prints 4
    print(next(my_iter))   # prints 5

def forLoop():
    my_list = [1, 2, 3, 4, 5]
    for item in my_list:
        print(item)

def whileLoop():
    count = 1
    while count < 6:
        print("Count:", count)
        count += 1

def breakWhileLoop():
    count = 1
    while count < 10:
        if count == 5:
            break
        print("Count:", count)
        count += 1

if __name__ == '__main__':
    selection = input('Select an example (1) iter function (2) for loop (3) while loop (4) break while loop: ')
    print('=' * 60)
    if selection == '1':
        iterFunction()
    elif selection == '2':
        forLoop()
    elif selection == '3':
        whileLoop()
    elif selection == '4':
        breakWhileLoop()
    else:
        print('Invalid input!')
    print('=' * 60)