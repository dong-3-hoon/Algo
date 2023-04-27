"""
노드 수
간선 정보
4
1 2 1 3 3 4 3 5
"""
n = 5

e = int(input())
tree = list(map(int, input().split()))

# 1. 인덱스 번호 -> 부모 노드의 번호
child_left = [0] * (n + 1)
child_right = [0] * (n + 1)

for i in range(e):
    parent = tree[i * 2]
    child = tree[i * 2 + 1]
    print(child)
    if child_left[parent] == 0:
        # 왼쪽 자식이 비어있으면 왼쪽에 추가
        child_left[parent] = child
    else:
        # 아니면 오른쪽에 추가
        child_right[parent] = child

print(child_left)
print(child_right)
print("--------------")
# 2. 인덱스 번호 -> 자식 노드의 번호
parent = [0] * (n + 1)
for i in range(e):
    p = tree[i * 2]
    c = tree[i * 2 + 1]
    parent[c] = p

print(parent)

# 5번 노드의 조상 노드 탐색
now = 5
# parent[now] == 0: 현재 위치가 root노드이기 때문에 부모 노드 존재 x
while parent[now] != 0:
    print(parent[now])
    now = parent[now]
