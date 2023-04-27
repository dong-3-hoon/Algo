import json
import os

def max_revenue(movies):
    pass
    filelist=os.listdir('data/movies')
    movie_revenue={}
    movie_title={}
    for i in filelist:
        #파일 경로를 str로 만듬
        filename='data/movies/'
        filename+=i

        #만들어진 str로 json파일을 open
        jsonfile=open(filename, encoding='utf-8')
        jsonfile_list=json.load(jsonfile)

        #values를 통해 key를 찾기 위해서 values: key로 만들어진 dic 생성
        movie_title[jsonfile_list['title']]=jsonfile_list['revenue']
        movie_revenue[jsonfile_list['revenue']]=jsonfile_list['title']
        
    #revenue가 높은 값의 영화 제목을 출력
    goodmovie=max(movie_title.values())
    return movie_revenue[goodmovie]
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
