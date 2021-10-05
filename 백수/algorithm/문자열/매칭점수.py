from collections import defaultdict
import re
def solution(word, pages):
    answer = defaultdict(list)
    word = word.lower()

    for idx,page in enumerate(pages):
        page = page.lower()
        word_cnt = 0
        external_sites = []
        my_site = re.findall('<meta property="og:url" content="\S+"',page)[0]
        my_site=my_site.split('"')[-2]
        
        external_sites = re.findall('<a href="\S+"',page)
        for i,site in enumerate(external_sites):
            external_sites[i]=site.split('"')[-2]

        s = re.sub("[^a-z]"," ",page).split()
        for c in s:
            if c == word:
                word_cnt+=1
        if my_site not in answer:
            answer[my_site] = [float(word_cnt),idx]
        else:
            answer[my_site][0] += word_cnt
            answer[my_site][1] = idx
        for site in external_sites:
            if site not in answer:
                answer[site] = [word_cnt/len(external_sites),-1]
            else:
                answer[site][0] += word_cnt/len(external_sites)
    answer = sorted(answer.items(),key = lambda x:(-x[1][0],x[1][1]))
    for a in answer:
        if a[1][1] != -1:
            return a[1][1]