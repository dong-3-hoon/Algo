def bubble_sort(a, N):
    # 각 원소를 비교
    for i in range(N):
        for j in range(N):
            # 원소의 자리가 다르고, 오른쪽 값이 크다면
            if i != j and a[i] < a[j]:
                # 교환
                a[i], a[j] = a[j], a[i]


arr = [55, 7, 78, 12, 42]

bubble_sort(arr, len(arr))
print(arr)
