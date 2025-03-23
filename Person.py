class Person:
    def __init__(self, name, age, height):

        self.__name = name
        self.__age = age
        self.__height = height
        self.public_prop="i'm public"

        print("constructing the person object")

    def __del__(self):
        print("The garbage collector is automatically destroying the Person object")

    #basic getter/setter
    #def get_name(self):
    #    return self.__name

    #def set_name(self, name):
    #    self.__name = name

    #Magic getter/setter
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # Magic getter/setter
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age


    #Magic getter/setter
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height



#p1 = Person("John",22,21)

#print(p1.public_prop)

#print(p1.__name) # doesnt work
#print(p1.name) # doesnt work


#print(p1.get_name)
#print(p1.get_name()) # works
#p1.set_name("jame")
#p1.name = "jake"
#print(p1.name)
#print(Person.get_name(p1))

#print(p1.height)
#p1.height=5
#print(p1.height)





#p1.name = "John"
#print(p1.name)
#print(p1.get_name())


#print("script is ending")