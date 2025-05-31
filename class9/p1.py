#inheritence

class Animal:
  def __init__(self,name):
    self.name = name
  def speak(self):
    raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
  def speak(self):
    return self.name + ' says woof!'

class Cat(Animal):
  def speak(self):
    return self.name + ' says meow!'

mydog = Dog("Buddy")
print(mydog.speak())

mycat = Cat("Tom")
print(mycat.speak())
