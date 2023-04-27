import sys

# from pprint import pprint
sys.stdin = open("daily/230222/16691.txt")

T = int(input())

for tc in range(1, T + 1):
    # A는 간선 갯수 B 는 노드 번호
    e, n = map(int, input().split())
    tree = list(map(int, input().split()))
    stk = [n]
    # 1. 인덱스 번호 -> 부모 노드의 번호
    child_left = [0] * (e + 2)
    child_right = [0] * (e + 2)

    for i in range(e):
        parent = tree[i * 2]
        child = tree[i * 2 + 1]
        if parent in stk:
            stk.append(child)
        if child_left[parent] == 0:
            # 왼쪽 자식이 비어있으면 왼쪽에 추가
            child_left[parent] = child
        else:
            # 아니면 오른쪽에 추가
            child_right[parent] = child
    print(f"#{tc} {len(stk)}")
