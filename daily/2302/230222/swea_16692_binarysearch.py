import sys

# from pprint import pprint
sys.stdin = open("daily/230222/16692.txt")


T = int(input())


# 중위 순회
def inorder(t):
    global cnt
    if t:
        # 왼쪽 방문
        cnt += 1
        inorder(cleft[t])
        cnt -= 1
        # 데이터 처리
        # print(t, end=" ")
        visited.append(t)

        # 오른쪽 방문
        cnt += 1
        inorder(cright[t])
        cnt -= 1


for tc in range(1, T + 1):
    n = int(input())
    lst = [i for i in range(n + 1)]
    tree = []
    cnt = 0
    k, i = 1, 1
    visited = []
    # 트리를 생성
    while i + k <= n:
        tree.append(i)
        tree.append(i + k)
        k += 1
        if i + k >= n:
            break
        tree.append(i)
        tree.append(i + k)
        i += 1
    # 인덱스가 부모 노드의 번호
    cleft = [0] * (n + 1)
    cright = [0] * (n + 1)
    if n % 2 == 0:
        for i in range(n - 1):
            p = tree[i * 2]
            c = tree[i * 2 + 1]
            if cleft[p] == 0:
                cleft[p] = c
            else:
                cright[p] = c
    else:
        for i in range(n - 2):
            p = tree[i * 2]
            c = tree[i * 2 + 1]
            if cleft[p] == 0:
                cleft[p] = c
            else:
                cright[p] = c

    inorder(1)
    print(f"#{tc} {visited.index(1) + 1} {visited.index(n // 2) + 1}")
