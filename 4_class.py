# Python Tutorial - Class

class ClassPerson_1:
    pass


class ClassPerson_2:
    name = "Joe"
    age = 42

class ClassPerson_3:
    name = "Joe"
    age = 42
    greeting = 'Hello!'

    def showName(self):
        print(self.name)

    def assignAge(self, age):
        self.age = age

    def sayHi(self):
        return self.greeting 
    
    def selfIntroduce(self):
        print(f'Hello, my name is {self.name}!')

'''
    Inheritance: 
            Inheritance is a way to create a new class that is a modified version of an existing class. 
            The new class is called a subclass, and the existing class is called the superclass. 
            The subclass inherits all the attributes and methods of the superclass, and can also have its own attributes and methods.
'''
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")


if __name__ == '__main__':
    selection = input('Select an example (1) Person (2) Animal: ')
    print('=' * 60)
    if selection == '1':
        # Create an object of ClassPerson_3
        person = ClassPerson_3()
        print('person.name: ', person.name)
        print('person.age: ', person.age)
        person.showName()
        person.assignAge(age = 3)
        print(person.sayHi())
        person.selfIntroduce()
    elif selection == '2':
        dog = Dog()
        dog.make_sound()
        cat = Cat()
        cat.make_sound()
    else:
        print('Invalid input!')
    print('=' * 60)