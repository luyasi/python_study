class Person:
    def __init__(self, gun):
        self.gun = gun

    def shoot(self, n):
        self.gun.fire(n)

    def reload(self, count):
        self.gun.bullit.bull_count += count
