class Card(object):
    def __init__(self, cardid, passwd, money):
        self.cardid = cardid
        self.passwd = passwd
        self.money = money
        self.islock = False
