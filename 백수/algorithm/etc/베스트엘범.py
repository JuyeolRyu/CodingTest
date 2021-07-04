#https://programmers.co.kr/learn/courses/30/lessons/42579
import operator
def solution(genres, plays):
    answer = []
    album = {}
    genre_li = {}
    for i in range(len(genres)):
        if genres[i] in album:
            album[genres[i]].append([plays[i],i])
            genre_li[genres[i]] += plays[i]
        else:
            album[genres[i]] = [[plays[i],i]]
            genre_li[genres[i]] = plays[i]
    
    #많이 재생된 장르 순으로 정렬
    genre_li = sorted(genre_li.items(),key=operator.itemgetter(1),reverse=True)

    for a in album:
        album[a] = sorted(album[a],key=lambda x:(x[0],-x[1]),reverse=True)

    for g in genre_li:
        g = g[0]
        for num,i in album[g][:2]:
            answer.append(i)

    return answer