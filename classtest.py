class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayInfo(self):
        # print("my name is %s, I'm %d" % (self.name, self.age))
        print("my name is {},I'm {}".format(self.name, self.age))


user1 = User('lily', 20)
user2 = User('tom', 28)

user1.sayInfo()
user2.sayInfo()
