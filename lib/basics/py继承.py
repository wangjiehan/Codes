class Animal(object):
    def __init__(self, name, sex, old):
        self.name = name
        self.sex = sex
        self.old = old

    def eat(self):
        print("吃~~~~~~")


class Cat(Animal):
    def __init__(self, name, sex, old, num):
        # 不需要写父类名,也不要写self
        super().__init__(name, sex, old)
        self.num = num

    def eat(self):
        super().eat()
        return "疯狂的吃!!!!"


wc = Cat("wc", '女', 4, '普通')
print(wc.eat())
print(wc.__class__)
