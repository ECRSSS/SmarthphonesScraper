
class Item:
    def __init__(self, name,url,prices,shopName):
        self.name=name
        self.url=url
        self.prices=prices
        self.shopName=shopName

    def to_string(self):
        return (self.name+" ").join(self.prices)+" "+self.shopName+" "+self.url