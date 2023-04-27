import sys
import copy
sys.stdin = open('grade2.txt')

T = int(input())
for tc in range(1, T+1):
    #성적 리스트
    grade_lst = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    #학생 수, 알고 싶은 학생 번호
    stu, ser_stu = map(int, input().split())
    #학생들 성적 저장
    stu_grade = []
    want = 0
    for i in range(stu):
        A = list(map(int, input().split()))
        stu_grade.append(A)
    #학생들 성적을 계산값으로 전환
    for i in range(len(stu_grade)):
        K = stu_grade[i][0]*0.35+stu_grade[i][1]*0.45+stu_grade[i][2]*0.2
        stu_grade[i] = K
    #내가 알고 싶은 학생의 점수
    want = stu_grade[ser_stu-1]
    #각각의 성적을 학점순으로 배치 - 딕셔너리로
    sort_grade = copy.deepcopy(stu_grade)
    sort_grade.sort(reverse = True)
    dict_grade = {}
    for i in sort_grade:
        dict_grade[i] = '0'
    #딕셔너리에 성적에 맞는 학생들의 성적 삽입
    # print(sort_grade)
    # print(grade_lst)
    # print(dict_grade)
    #grade lst는 10으로 고정, sort, dict 는 20, 30 정도라서 안 됨 그러면

    for i in range(len(sort_grade)):
        dict_grade[sort_grade[i]] = grade_lst[i]
    print(dict_grade)
    print(dict_grade[want])