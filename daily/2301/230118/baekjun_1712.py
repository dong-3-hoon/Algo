a, b, c=map(int, input().split())
if b<c and a>0 and b>0 and c>0:
    cnt=(a/(c-b)+1)
    print(int(cnt))
else:
    print(-1)