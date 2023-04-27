import sys

# from pprint import pprint
sys.stdin = open("daily/230220/1225.txt")

tc = 1


#  item 을 큐에 삽입하고 rear을 +시킴, 범위가 넘어간다면 0으로 바꿔줌
def enqueue(item):
    global rear
    rear = (rear + 1) % size
    cq[rear] = item


# 큐 맨 앞에 있는 원소를 리턴
def dequeue():
    global front
    front = (front + 1) % size
    return cq[front]


while tc < 11:
    # 최초 위치는 front, rear 모두 0
    front = rear = 0
    m = int(input())
    lst = list(map(int, input().split()))
    # 크기는 배열 길이 + 1
    size = len(lst) + 1
    cq = [0] * size
    # 배열에 있는 원소들을 큐에 삽입
    for i in lst:
        enqueue(i)
    stk = 1
    while True:
        # 큐 맨 앞에 있는 원소를 k에 넣고
        k = dequeue()
        # stk 만큼 뺀 후 큐 맨 뒤에 삽입
        enqueue(k - stk)
        # 계산 결과가 0 이하이면 반복을 종료
        if k - stk <= 0:
            cq[rear] = 0
            break
        # stk 가 5에서 반복
        stk += 1
        if stk == 6:
            stk = 1
    print(f"#{tc}", end=" ")
    # 계산 결과 8가지를 큐에서 빼옴
    for i in range(8):
        print(dequeue(), end=" ")
    print()
    tc += 1
