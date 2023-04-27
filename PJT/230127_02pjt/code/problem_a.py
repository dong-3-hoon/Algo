'''
# requests 사용 예시 1

import requests


URL = 'https://dog.ceo/api/breeds/image/random'

response = requests.get(URL).json()
print(response)

results = response.get('message')
print(results)
'''
import requests


def popular_count():
    pass 
    cnt=0
    # 여기에 코드를 작성합니다.  
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=d838f386c11255ef5f578f676243694f'
    response = requests.get(URL).json()
    for i in response['results']:
        cnt+=1
    return cnt
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
