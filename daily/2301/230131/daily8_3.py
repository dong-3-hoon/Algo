class PublicTransport:
    getin = 0
    getout = 0
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare
    def get_in(self, passenger):
        PublicTransport.getin += passenger
        return PublicTransport.getin

    def get_off(self, passenger):
        PublicTransport.getout += passenger
        return PublicTransport.getin-PublicTransport.getout

    def profit(self):
        print(self.fare * (PublicTransport.getin-PublicTransport.getout))

train = PublicTransport('기차', 3000)
airplain = PublicTransport('비행기', 5000)

print(train.get_in(20))
print(train.get_off(5))
train.profit()