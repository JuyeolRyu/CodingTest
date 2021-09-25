def solution(n, words):
    answer = [0,0]
    dic = []
    for i,word in enumerate(words):
        if word not in dic:
            if dic and words[i-1][-1] != word[0]:
                return([(i)%n+1,i//n+1])
            dic.append(word)
        else:
            return([(i)%n+1,i//n+1])

    return answer