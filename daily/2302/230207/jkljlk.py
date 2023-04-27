###binary search
def binary_search(arr, n, key):
    # 검색 범위를 지정
    #시작, 끝
    start = 0
    end = n-1

    while start <= end:
        # 가운데를 선택
        mid = (start + end) // 2
        # 가운데에 내가 찾는 게 있다
        if arr[mid] == key:
            #탐색 성공
            print(f"find")
            return mid
        #가운데 값이 내가 찾는 값보다 크다
        elif arr[mid]>key:
            #검색 범위 재지정
            #오른쪽은 더이상 살펴볼 필요가 없다. 뒤는 어차피 나보다 큼
            #검색의 끝 범위를 가운데로 땡겨옴
            end = mid -1
        else:
            #왼쪽은 나보다 작아서 필요없음
            #검색의 시작 범위를 가운데로 땡겨옴
            start = mid + 1
    print('cant find')
    return -1

arr=[2,3,5,7,8,16,77]
n = len(arr)
binary_search(arr, n, 16)