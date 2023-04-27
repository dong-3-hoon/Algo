import json
import os

def dec_movies(movies):
    movie_R_D={}
    movie_T={}
    dec_M=[]
    pass 

    # 여기에 코드를 작성합니다.  
    filelist=os.listdir('data/movies')
    
    for i in filelist:
        #파일 경로를 str로 만듬
        filename='data/movies/'
        filename+=i

        #만들어진 str로 json파일을 open
        jsonfile=open(filename, encoding='utf-8')
        jsonfile_list=json.load(jsonfile)

        #releadate와 title를 받아와서 각 key, values에 할당된 dict 2개를 생성
        movie_T[jsonfile_list['title']]=jsonfile_list['release_date']
        movie_R_D[jsonfile_list['release_date']]=jsonfile_list['title']

    #release date에서 월에 해당하는 [5:7]을 문자열에 추가하고 해당하는 제목을 dec_M list에 추가 후 리턴
    for i in movie_R_D:
        stk=''
        for j in i[5:7]:
            stk+=j
        if stk=='12':
            dec_M.append(movie_R_D[i])
    return dec_M


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
