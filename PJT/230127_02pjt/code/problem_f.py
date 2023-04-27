import requests
from pprint import pprint
#영화 진흥 위원회
def kofic(service):
    #박스오피스 순위
    if service==1:
        URL='http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=1c0b64834140bdabaf80f06d2f862825&targetDt=20230126'
        response = requests.get(URL).json()
        response=response['boxOfficeResult']
        response=response['dailyBoxOfficeList']
        cnt=0
        print('영화 순위')
        for i in response:
            for j in i:
                if j=='movieNm':
                    cnt+=1
                    print(f'{cnt}위 {i[j]}')
    #영화 정보 출력
    else:
        movie_name=input('영화 이름을 입력하시오:')
        URL=f'http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=1c0b64834140bdabaf80f06d2f862825&movieNm={movie_name}'
        response = requests.get(URL).json()
        response = response['movieListResult']
        response = response['movieList']
        for value in response:
            for real_value in value:
                if real_value=='movieNm' and value[real_value]==movie_name:
                    movie_code=value['movieCd']
        N_URL=f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=1c0b64834140bdabaf80f06d2f862825&movieCd={movie_code}'
        response2 = requests.get(N_URL).json()
        response2 = response2['movieInfoResult']
        response2 = response2['movieInfo']
        for key in response2['directors']:
            for value in key:
                if value=='peopleNm':
                    print(f'감독 이름: {key[value]}')
        cnt=0
        for key in response2['actors']:
            for value in key:
                if value=='peopleNm':
                    print(f'주연: {key[value]}')
                    cnt+=1
                if cnt==5:
                    break
            if cnt==5:
                break

#TMDB
def tmdb(service):
    #박스오피스 순위
    if service==1:
        URL = 'https://api.themoviedb.org/3/movie/popular?api_key=d838f386c11255ef5f578f676243694f'
        response = requests.get(URL).json()
        response = response['results']
        cnt=0
        for movie in response:
            for key in movie:
                if key=='title':
                    cnt+=1
                    print(f'{cnt}위 {movie[key]}')
                if cnt==10:
                    break
    else:
        reco_movie_list=[]
        movie_name=input('영화 이름을 입력하시오:')
        URL = f'https://api.themoviedb.org/3/search/movie?api_key=d838f386c11255ef5f578f676243694f&query={movie_name}'
        response = requests.get(URL).json()
        for i in response['results'][0]:
            if i=='id':
                movie_id=response['results'][0][i]
        URL2=f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=d838f386c11255ef5f578f676243694f&query='
        response = requests.get(URL2).json()
        cnt=0
        for crew_person in response['crew']:
            if crew_person['department']=='Directing':
                cnt+=1
                print(f'감독: {crew_person["name"]}')
                if cnt==1:
                    break

        cnt=0
        for cast_person in response['cast']:
            if cast_person['cast_id']<10:
                cnt+=1
                print(f'주연: {cast_person["name"]}')



print('영화 정보를 불러올 사이트의 번호를 선택하십시오')
print('1. 영화 진흥 위원회')
print('2. The Movie DB')
api_site = int(input())

print('일람하고 싶은 서비스를 선택하세요')
print('1. 박스 오피스 순위')
print('2. 영화 검색 서비스')
service = int(input())

if api_site==1:
    kofic(service)
else:
    tmdb(service)