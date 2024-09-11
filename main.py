'''
class Person:
    def say_hello(self):
        print("Hello!")

tom=Person()
tom.say_hello()
'''
'''
class Person:
    def say(self,message):
        print(message)

tom=Person()
tom.say("Hello ,brotha! ")
'''
'''
class Person:
    def say(self,message):
        print(message)
    def say_hello(self):
        self.say("Hello work") 

tom=Person()
tom.say_hello()
'''
'''
class Person:
    def __init__(self,name):
        self.name=name
       