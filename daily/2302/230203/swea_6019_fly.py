"""D1 = 250
Train1 = 10
Train2 = 15
F = 20
t = 0
fly_to_t2_speed = Train2 + F
fly_to_t1_speed = Train1 + F
t1_t2_distance = 250 - (Train1 +Train2)*t
dis = []
f_dis = []
while t1_t2_distance > 0:
    t1_t2_distance = 250 - (Train1 + Train2) * t
    print(t1_t2_distance)
    if t % 2 == 0:
        f_dis.append(t1_t2_distance/fly_to_t2_speed*F)
    else:
        f_dis.append(t1_t2_distance/fly_to_t1_speed*F)
    t += 1
print(f_dis)
"""

"""
T1 = 0
T2 = 250
x= 시간
T1 = 10x
T2 = -15x
10초 후 부딪힘
20 * 10

"""

T = int(input())

for tc in range(1, T+1):
    Dis, T1, T2, Fly = map(int, input().split())
    t = (Dis/(T1 + T2))*Fly
    print(f'#{tc} {t}')