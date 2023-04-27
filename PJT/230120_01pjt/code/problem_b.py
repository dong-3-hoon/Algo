import json
from pprint import pprint



def movie_info(movie, genres):
    pass 
    #기존 id를 리스트에 저장
    genre_id=[]

    #id를 기준으로 genre_detail에서 장르를 추출
    genre_name=[]

    #필요한 정보를 담을 리스트를 생성
    print_movie={'id':0, 'title':'', 'poster_path':'', 'vote_average':0, 'overview':'', 'genre_ids':[]}

    #기존 영화 키와 리턴할 키가 같다면 리턴 키에 정보 넣기
    for i in print_movie.keys():
        print_movie[i]=movie[i]

    #장르 아이디와 장르 디테일의 아이디 숫자가 같다면 name을 추가
    for i in genres:
        for j in print_movie['genre_ids']:
            if i['id']==j:
                genre_name.append(i['name'])
                
    #장르 아이디 키 삭제 후 장르 네임 키 삽입
    del print_movie['genre_ids']
    print_movie['genre_name']=genre_name

    return print_movie

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
