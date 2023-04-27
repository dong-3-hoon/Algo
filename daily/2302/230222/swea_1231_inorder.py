import sys

# from pprint import pprint
sys.stdin = open("daily/230222/1231.txt")


def inorder(v):
    global num  # num 은 1부터 차례대로 할당하고, 할당하면 1씩 증가
    # v번 노드가 존재하면 ( 트리 범위 안에 있다면 )
    if v <= word:
        # 왼쪽 자식에 할당 ( v * 2 )
        inorder(v * 2)
        # 자기 자신에 할당, num 1 증가
        tree[v] = num
        print(arr[v][1], end="")
        num += 1
        # 오른쪽 자식에 할당 ( v * 2 + 1)
        inorder(v * 2 + 1)


tc = 1
while tc < 11:
    arr = [[]]
    word = int(input())
    tree = [0] * (word + 1)
    for i in range(word):
        lst = list(input().split())
        arr.append(lst)
    num = 1
    print(f"#{tc}", end=" ")
    inorder(num)
    print()
    tc += 1
