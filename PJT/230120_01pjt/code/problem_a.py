import json
from pprint import pprint


def movie_info(movie):
    pass
    # 영화 정보를 변수에 저장      
    movie = open('data/movie.json', encoding='utf-8')
    movie_detail = json.load(movie)

    #필요한 정보를 담을 리스트를 생성
    print_movie={'id':0, 'title':'', 'poster_path':'', 'vote_average':0, 'overview':'', 'genre_ids':[]}
    
    #기존 영화 키와 리턴할 키가 같다면 리턴 키에 정보 넣기
    for i in print_movie.keys():
        print_movie[i]=movie_detail[i]
    return print_movie

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
