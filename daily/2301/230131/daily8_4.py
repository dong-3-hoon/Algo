class PublicTransport:
    maxseat=20
    getin = 0
    getout = 0
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare
    def get_in(self, passenger):
        PublicTransport.getin += passenger
        if PublicTransport.maxseat<PublicTransport.getin:
            return print('더이상 탑승할 수 없습니다')
        return PublicTransport.getin

    def get_off(self, passenger):
        PublicTransport.getout += passenger
        return PublicTransport.getin-PublicTransport.getout

    def profit(self):
        print(self.fare * (PublicTransport.getin-PublicTransport.getout))

Bus = PublicTransport('bus', 500)
Bus.get_in(10)
Bus.get_in(15)