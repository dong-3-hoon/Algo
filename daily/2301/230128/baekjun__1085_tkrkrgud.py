nowx, nowy, squrex, squrey = map(int, input().split())
comp = []

comp.append(nowx)
comp.append(nowy)
comp.append(squrex-nowx)
comp.append(squrey-nowy)

print(min(comp))