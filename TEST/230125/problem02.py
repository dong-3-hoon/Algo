# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 min, max 사용 금지
def min_max(scores):
    pass
    # answer 튜플 생성
    answer=()
    sort_score=[]
    #scores를 정렬시킨 후
    sort_score=sorted(scores)
    #최대값인 scores[0], 최솟값인 scores[-1]을 넣는다
    answer=sort_score[0], sort_score[-1]
    return answer
    #리턴값이 여러개면 알아서 튜플로 묶어서 리턴해줌


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(min_max(scores))    # (75, 90)
