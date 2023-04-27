import sys

# from pprint import pprint
sys.stdin = open("daily/230223/16270.txt")


def postorder(t):
    # 트리의 범위 밖이면
    # return 0

    # 트리의 범위 안이면
        # 현재 내 값(tree[t])이 0이 아니면
        # return tree[t]
        # 0 이면 계산
        left = postorder(?)
        right = postorder(?)
        tree[t] = left + right
        return tree[t]

# 1번부터 후위 순회 한뒤에 tree[L] 값 출력