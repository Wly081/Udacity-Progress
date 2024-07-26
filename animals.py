class Dog:
    def speak(self):
        print("Woof!")

    def __init__(self, name):
        self.name = name

    def hear(self, words):
        if self.name in words:
            self.speak()


class Husky(Dog):
    origin = "Siberia"

    def speak(self):
        print("Awoo!")


class Chihuahua(Dog):
    origin = "Mexico"

    def speak(self):
        print("Yip!")


class Labrador(Dog):
     origin = "Canada"