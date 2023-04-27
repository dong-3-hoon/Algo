num = int(input())
lst = list(map(int, input().split()))
m_grade = max(lst)

for i in range(num):
    lst[i] = lst[i] / m_grade * 100
print(sum(lst) / len(lst))
