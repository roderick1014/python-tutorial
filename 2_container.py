# Python Tutorial - Container

def listExample():
    '''
        Lists:
                Lists are ordered collections of items that can be of any type.
                You can create a list using square brackets [] or the list() function.
    '''

    # Creating a list
    my_list = [1, 2, 3, 4, 5]
    print('Create my_list: ', my_list)

    # Accessing elements
    print('Accessing elements -> my_list[0]: ', my_list[0])  # Output: 1

    # Modifying elements
    my_list[2] = 10
    print('Modifying the element my_list[2] = 10: ', my_list)  # Output: [1, 2, 10, 4, 5]

    # Appending elements
    my_list.append(6)
    print('Appending a element my_list.append(6): ', my_list)  # Output: [1, 2, 10, 4, 5, 6]

    # Slicing
    print('Slicing my_list[1:4]: ',my_list[1:4])  # Output: [2, 10, 4]



def tupleExample():
    '''
        Tuples:
                Tuples are similar to lists but are immutable, meaning they cannot be modified once created.
                Tuples are defined using parentheses () or the tuple() function.
    '''

    # Creating a tuple
    my_tuple = (1, 2, 3, 4, 5)
    print('Create my_tuple: ', my_tuple)

    # Accessing elements
    print('Accessing elements -> my_tuple[0]: ', my_tuple[0])  # Output: 1

    # Slicing
    print('Slicing my_tuple[1:4]: ', my_tuple[1:4])  # Output: (2, 3, 4)



def setExample():
    '''
        Sets:
            Sets are unordered collections of unique elements.
            Sets are defined using curly braces {} or the set() function.
    '''

    # Creating a set
    my_set = {1, 2, 3, 4, 5}
    print('Create my_set: ', my_set)

    # Adding elements
    my_set.add(6)
    print('Adding a element 6: ', my_set)  # Output: {1, 2, 3, 4, 5, 6}
    

    # Removing elements
    my_set.remove(3)
    print('Removing a element 3: ', my_set)  # Output: {1, 2, 4, 5, 6}



def dictionaryExample():
    '''
            Dictionaries:
                Dictionaries are unordered collections of key-value pairs.
                Each value is associated with a unique key that can be used to access it.
                Dictionaries are defined using curly braces {} or the dict() function.
    '''

    # Creating a dictionary
    my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
    print('Create my_dict: ', my_dict)

    # Accessing values
    print('Accessing a value -> my_dict["name"]: ', my_dict['name'])  # Output: John

    # Modifying values
    my_dict['age'] = 31
    print('Modifying a value -> my_dict["age"] = 31: ', my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

    # Adding new key-value pairs
    my_dict['occupation'] = 'Engineer'
    print('Adding new key-value paris -> my_dict["occupation"] = "Engineer": ', my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'occupation': 'Engineer'}

if __name__ == '__main__':
    selection = input('Choose a container to display: (1) list (2) tuple (3) set (4) dictionary: ')
    print('=' * 60)
    if selection == '1':
        listExample()
    elif selection == '2':
        tupleExample()
    elif selection == '3':
        setExample()
    elif selection == '4':
        dictionaryExample()
    else:
        print('Invalid selection!')
    print('=' * 60)