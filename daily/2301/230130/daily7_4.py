class fee:
    def __init__(self, time, dist):
        self.time = time
        self.dist = dist
        div30 = time / 30
        if int(div30) != div30:
            div30 = div30//30
            div30 += 1
        if dist>100:
            print((time // 10 * 1200) + ((100*170) +((dist-100)*(170/2)))+(div30*525))
        else:
            print((time // 10 * 1200) + (dist*170) +(div30*525))

fee(600, 50) #=> 91000 대여시간, 주행 거리
fee(600, 110) #=> 10

