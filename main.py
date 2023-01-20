class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name, age, isHappy): #constructor
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, name = None, age = None, isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

        self.get_data()

    def get_data(self):
        print("name:", self.name, "age:", self.age, ".Happy:", self.isHappy)

cat1 = Cat("Barsik", 3, True)
cat1.set_data("John", 2)

cat2 = Cat("Jopen", 2, False)





