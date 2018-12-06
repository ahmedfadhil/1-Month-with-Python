class Animal:
    noise = "Grunt"
    size = "large"
    color = "brown"
    hair = 'cover body'

    def get_color(self):
        return self.color

    def make_noise(self):
        return self.noise


dog = Animal()
dog.make_noise()
dog.size = "small"
dog.color = "black"
dog.hair = "hairless"


class Dog(Animal):
    name = "Jon"
    # color = "brown"
    #
    # def get_color(self):
    #     return self.color


jon = Dog()
jon.color = "white"
jon.name = "Jon snow"

abc = "some text..."


def some_func(arg1, arg2, kwargs=abc):
    print(kwargs)


email_address = "some email address"
to_list = "some email address list"
from_list = "from some email address list"


def send_email(email=email_address, to_list=to_list, from_list=from_list):
    print(email, to_list, from_list)



@property
def make_noise(self):
    return self.noise



















