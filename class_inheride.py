class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale,exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater")  # this is an addon for fish class

    def swim(self):
        print("move in water")

a=Fish()
a.breathe()
a.swim()
print(a.num_eyes)