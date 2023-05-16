# Python Tutorial - Basic Syntax

# This is a single-line comment

'''
    This is a
    multi-line
    comment
'''

def variablesExample():
    # Variables
    print("Hello, World!")   # prints Hello, World!

    name = "John"   # string
    print('name: ', name, ', variable type: ', type(name))
    age = 25        # integer
    print('age: ', age, ', variable type: ', type(age))
    weight = 55.5   # float
    print('weight: ', weight, ', variable type: ', type(weight))
    is_student = True   # boolean
    print('is_student: ', is_student, ', variable type: ', type(is_student))

    name = "Alice"
    age = 30
    print("Name:", name, "Age:", age)   # prints Name: Alice Age: 30

def arithmeticOperators():
    # Arithmetic operators
    x = 10 + 5   # addition
    print('x = 10 + 5: ', x)
    y = 10 - 5   # subtraction
    print('y = 10 - 5: ', y)
    z = 10 * 5   # multiplication
    print('z = 10 * 5: ', z)
    w = 10 / 5   # division
    print('w = 10 / 5: ', w)
    remainder = 10 % 3   # modulus (remainder of division)
    print('remainder = 10 % 5: ', remainder)
    power = 2 ** 3   # exponentiation (2 raised to the power of 3)
    print('power = 2 ** 3: ', power)

def comparisonOperators():
    x = 3
    y = 2
    print('x: ', x, 'y: ', y)
    # Comparison operators
    is_equal = x == y   # equal to
    print('"is_equal = x == y" -> output: ', is_equal)
    is_not_equal = x != y   # not equal to
    print('"is_not_equal = x != y" -> output: ', is_not_equal)
    is_greater = x > y   # greater than
    print('"is_greater = x > y" -> output: ', is_greater)
    is_less = x < y   # less than
    print('"is_less = x < y" -> output: ', is_less)
    is_greater_equal = x >= y   # greater than or equal to
    print('"is_greater_equal = x >= y" -> output: ', is_greater_equal)
    is_less_equal = x <= y   # less than or equal to
    print('"is_less_equal = x <= y" -> output: ', is_less_equal)

def logicalOperator():
    # Logical operators
    logical_and = True and False   # logical AND
    print('"logical_and = True and False" -> output: ', logical_and)
    logical_or = True or False   # logical OR
    print('"logical_or = True or False" -> output: ', logical_or)
    logical_not = not True   # logical NOT
    print('"logical_not = not True" -> output: ', logical_not)

def conditionalOperator():
    age = int(input('Input your age: '))
    print('age: ', age)

    if age >= 18:
        print("You are an adult.")
    else:
        print("You are not an adult.")

if __name__ == '__main__':
    selection = input('Select an example (1) Variables (2) Arithmetic (3) Comparison (4) Logic (5) Condition : ')
    print('=' * 60)
    if selection == '1':
        variablesExample()
    elif selection == '2':
        arithmeticOperators()
    elif selection == '3':
        comparisonOperators()
    elif selection == '4':
        logicalOperator()
    elif selection == '5':
        conditionalOperator()
    else:
        print('Invalid selection!')
    print('=' * 60)