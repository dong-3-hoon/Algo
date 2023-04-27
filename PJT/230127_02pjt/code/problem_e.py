import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    reco_movie_list=[]
    URL = f'https://api.themoviedb.org/3/search/movie?api_key=d838f386c11255ef5f578f676243694f&query={title}'
    response = requests.get(URL).json()
    if response['results']==[]:
        return None
    for i in response['results'][0]:
        if i=='id':
            movie_id=response['results'][0][i]
    URL2=f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=d838f386c11255ef5f578f676243694f&query='
    response2 = requests.get(URL2).json()
    main_cast, main_crew=[], []
    cast_crew={}
    
    for cast_person in response2['cast']:
        if cast_person['cast_id']<10:
            main_cast.append(cast_person['name'])
    cast_crew['cast']=main_cast

    for crew_person in response2['crew']:
        if crew_person['department']=='Directing':
            main_crew.append(crew_person['name'])
    cast_crew['crew']=main_crew
    return cast_crew
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
