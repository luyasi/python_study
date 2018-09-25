class Gun():
    def __init__(self, bullit):
        self.bullit = bullit

    def fire(self, n):
        if n >= self.bullit.bull_count > 0:
            print("tu" * self.bullit.bull_count)
            print("子弹已经打完")
        elif self.bullit.bull_count > n:
            print("tu" * n)
            self.bullit.bull_count -= n
            print("还剩%s发子弹" % (self.bullit.bull_count))
        else:
            print("子弹不够请填充")
